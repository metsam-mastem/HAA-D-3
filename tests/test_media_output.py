import tempfile
import unittest
from pathlib import Path

from haa_d3.kuramoto import simulate_kuramoto
from haa_d3.scene_mappings import kuramoto_to_scene
from haa_d3.media import write_sonification_wav, render_scene_mp4


class MediaOutputTests(unittest.TestCase):
    def setUp(self):
        self.simulation = simulate_kuramoto(nodes=4, coupling=1.1, dt=0.25, steps=4, seed=13)
        self.scene = kuramoto_to_scene(self.simulation, frame_rate=4)

    def test_wav_sonification_is_valid_and_deterministic(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.wav"
            second = Path(directory) / "second.wav"
            write_sonification_wav(self.simulation, first)
            write_sonification_wav(self.simulation, second)
            self.assertEqual(first.read_bytes()[:12], b"RIFF" + (first.stat().st_size - 8).to_bytes(4, "little") + b"WAVE")
            self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_scene_renders_to_playable_mp4(self):
        with tempfile.TemporaryDirectory() as directory:
            audio = Path(directory) / "sonification.wav"
            video = Path(directory) / "preview.mp4"
            write_sonification_wav(self.simulation, audio)
            result = render_scene_mp4(self.scene, audio, video)
            payload = video.read_bytes()
            self.assertGreater(len(payload), 1000)
            self.assertIn(b"ftyp", payload[:32])
            self.assertEqual(result["status"], "RENDERED_NOT_REVIEWED")
            self.assertGreater(result["frame_count"], 0)
            self.assertEqual(result["verification"]["decode"], "PASS")
            self.assertTrue(result["verification"]["has_video"])
            self.assertTrue(result["verification"]["has_audio"])
            self.assertLessEqual(result["verification"]["audio_video_duration_delta_seconds"], 0.30)


if __name__ == "__main__":
    unittest.main()
