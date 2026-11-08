"""Optional MP4 assembly and deterministic WAV data-sonification."""
from __future__ import annotations

import json
import math
import shutil
import subprocess
import tempfile
import wave
from array import array
from pathlib import Path
from typing import Any

from .render_svg import render_scene_frames


def _normalized_samples(simulation: dict[str, Any]) -> list[tuple[float, float]]:
    if simulation.get("model") != "kuramoto_mean_field":
        raise ValueError("simulation must be a Kuramoto mean-field output")
    samples = simulation.get("samples")
    if not isinstance(samples, list) or len(samples) < 2:
        raise ValueError("simulation must contain at least two samples")
    normalized = []
    previous = None
    for sample in samples:
        time_value = float(sample["time_seconds"])
        coherence = float(sample["order_parameter"])
        if not math.isfinite(time_value) or time_value < 0:
            raise ValueError("sample times must be finite and non-negative")
        if previous is not None and time_value <= previous:
            raise ValueError("sample times must be strictly increasing")
        if not math.isfinite(coherence) or not 0 <= coherence <= 1.0000001:
            raise ValueError("order_parameter must be in [0, 1]")
        normalized.append((time_value, coherence))
        previous = time_value
    return normalized


def write_sonification_wav(
    simulation: dict[str, Any],
    output_path: Path,
    *,
    sample_rate: int = 22050,
) -> dict[str, Any]:
    """Synthesize short, windowed tones from r(t); this is sonification, not music."""
    if isinstance(sample_rate, bool) or not isinstance(sample_rate, int) or not 8000 <= sample_rate <= 48000:
        raise ValueError("sample_rate must be an integer in [8000, 48000]")
    samples = _normalized_samples(simulation)
    duration_tail = min(0.08, (samples[-1][0] - samples[-2][0]) * 0.8)
    total_duration = samples[-1][0] + duration_tail
    if total_duration <= 0 or total_duration > 120:
        raise ValueError("sonification duration must be in (0, 120] seconds")
    pcm = array("h", [0]) * math.ceil(total_duration * sample_rate)
    for index, (timestamp, coherence) in enumerate(samples):
        interval = samples[index + 1][0] - timestamp if index + 1 < len(samples) else samples[-1][0] - samples[-2][0]
        tone_duration = min(0.08, interval * 0.8)
        count = max(1, round(tone_duration * sample_rate))
        start = round(timestamp * sample_rate)
        pitch = max(48, min(84, 48 + round(coherence * 36)))
        velocity = max(1, min(127, 32 + round(coherence * 88)))
        frequency = 440.0 * (2.0 ** ((pitch - 69) / 12.0))
        amplitude = 0.24 * velocity / 127.0
        fade = max(1, round(0.005 * sample_rate))
        for offset in range(min(count, len(pcm) - start)):
            envelope = min(1.0, offset / fade, (count - offset - 1) / fade)
            value = int(32767 * amplitude * max(0.0, envelope) * math.sin(2 * math.pi * frequency * offset / sample_rate))
            pcm[start + offset] = max(-32768, min(32767, value))
    if pcm.itemsize != 2:
        raise RuntimeError("platform does not provide 16-bit array elements")
    if __import__("sys").byteorder != "little":
        pcm.byteswap()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output_path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(pcm.tobytes())
    return {
        "format": "WAV PCM signed 16-bit mono",
        "sample_rate_hz": sample_rate,
        "duration_seconds": round(len(pcm) / sample_rate, 6),
        "evidence_class": "MODEL_OUTPUT",
        "interpretation": "data sonification; not a composed soundtrack",
        "output": "sonification/coherence.wav",
    }


def render_scene_mp4(
    scene: dict[str, Any],
    audio_path: Path,
    output_path: Path,
    *,
    frame_rate: float | None = None,
) -> dict[str, Any]:
    """Rasterize SVG frames with CairoSVG and assemble MP4 with FFmpeg."""
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("FFmpeg is required for MP4 export; install ffmpeg and retry")
    try:
        import cairosvg
    except ImportError as exc:
        raise RuntimeError("CairoSVG is required for MP4 export; install haa-d3[media]") from exc
    if not audio_path.is_file():
        raise FileNotFoundError(f"audio file not found: {audio_path}")
    raw_fps = frame_rate if frame_rate is not None else scene["frame_rate"]
    if isinstance(raw_fps, bool) or not isinstance(raw_fps, (int, float)) or not math.isfinite(raw_fps) or raw_fps <= 0 or raw_fps > 120:
        raise ValueError("frame_rate must be finite and in (0, 120]")
    fps = float(raw_fps)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="haa-d3-mp4-") as temporary:
        root = Path(temporary)
        svg_paths = render_scene_frames(scene, root / "svg", frame_rate=fps)
        png_dir = root / "png"
        png_dir.mkdir()
        for index, svg in enumerate(svg_paths):
            cairosvg.svg2png(url=str(svg), write_to=str(png_dir / f"frame_{index:06d}.png"))
        command = [
            ffmpeg, "-y", "-hide_banner", "-loglevel", "error",
            "-framerate", str(fps), "-i", str(png_dir / "frame_%06d.png"),
            "-i", str(audio_path), "-c:v", "libx264", "-preset", "veryfast",
            "-crf", "23", "-pix_fmt", "yuv420p", "-c:a", "aac",
            "-b:a", "128k", "-shortest", "-movflags", "+faststart",
            str(output_path),
        ]
        completed = subprocess.run(command, capture_output=True, text=True, timeout=300)
        if completed.returncode != 0:
            raise RuntimeError(f"FFmpeg failed: {completed.stderr[-2000:]}")
    if not output_path.is_file() or output_path.stat().st_size < 1000:
        raise RuntimeError("FFmpeg did not produce a valid MP4 output")

    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        raise RuntimeError("FFprobe is required to verify MP4 stream metadata")
    probe = subprocess.run(
        [ffprobe, "-v", "error", "-show_entries",
         "format=duration:stream=codec_type,codec_name,width,height,duration",
         "-of", "json", str(output_path)],
        capture_output=True, text=True, timeout=60,
    )
    if probe.returncode != 0:
        raise RuntimeError(f"FFprobe failed: {probe.stderr[-2000:]}")
    try:
        probe_data = json.loads(probe.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("FFprobe returned invalid JSON") from exc
    streams = probe_data.get("streams", [])
    video_stream = next((item for item in streams if item.get("codec_type") == "video"), None)
    audio_stream = next((item for item in streams if item.get("codec_type") == "audio"), None)
    if video_stream is None or audio_stream is None:
        raise RuntimeError("MP4 must contain both video and audio streams")
    if video_stream.get("codec_name") != "h264" or audio_stream.get("codec_name") != "aac":
        raise RuntimeError("MP4 codecs do not match the required H.264/AAC profile")
    if not isinstance(video_stream.get("width"), int) or not isinstance(video_stream.get("height"), int):
        raise RuntimeError("MP4 video dimensions are missing")
    format_duration = float(probe_data.get("format", {}).get("duration", 0))
    if not math.isfinite(format_duration) or format_duration <= 0:
        raise RuntimeError("MP4 duration metadata is invalid")
    decoded = subprocess.run(
        [ffmpeg, "-v", "error", "-xerror", "-i", str(output_path), "-f", "null", "-"],
        capture_output=True, text=True, timeout=120,
    )
    if decoded.returncode != 0:
        raise RuntimeError(f"MP4 decode verification failed: {decoded.stderr[-2000:]}")
    verification = {
        "decode": "PASS",
        "has_video": True,
        "has_audio": True,
        "video_codec": video_stream["codec_name"],
        "audio_codec": audio_stream["codec_name"],
        "width": video_stream["width"],
        "height": video_stream["height"],
        "container_duration_seconds": format_duration,
    }
    return {
        "status": "RENDERED_NOT_REVIEWED",
        "container": "MP4",
        "video_codec": "H.264",
        "audio_codec": "AAC",
        "frame_rate": fps,
        "frame_count": len(svg_paths),
        "verification": verification,
        "evidence_class": scene.get("metadata", {}).get("evidence_class", "UNKNOWN"),
        "output": "video/preview.mp4",
    }
