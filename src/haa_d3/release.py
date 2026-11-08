"""Build a reproducible, inspectable HAA-D-3 vertical-slice release bundle."""
from __future__ import annotations

import hashlib
import json
import tempfile
import zipfile
from pathlib import Path
from typing import Any

from .contracts import validate_scene
from .schema_validation import validate_json_schema
from .render_svg import render_scene_frames
from .sonification import write_sonification_midi
from .media import write_sonification_wav, render_scene_mp4


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_release_bundle(
    simulation: dict[str, Any],
    scene: dict[str, Any],
    output_path: Path,
    *,
    include_video: bool = False,
) -> Path:
    """Create ZIP with simulation, SceneSpec, SVG frames, MIDI and hash manifest."""
    schema_errors = validate_json_schema(scene, "scene-spec.schema.json")
    semantic_errors = validate_scene(scene)
    if schema_errors or semantic_errors:
        raise ValueError("invalid SceneSpec: " + "; ".join(schema_errors + semantic_errors))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="haa-d3-release-") as temporary:
        root = Path(temporary)
        (root / "frames").mkdir()
        (root / "sonification").mkdir()
        (root / "simulation.json").write_text(
            json.dumps(simulation, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        (root / "scene.json").write_text(
            json.dumps(scene, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        render_scene_frames(scene, root / "frames")
        sonification = write_sonification_midi(simulation, root / "sonification" / "coherence.mid")
        wav_metadata = None
        video_metadata = {"status": "NOT_REQUESTED"}
        if include_video:
            wav_metadata = write_sonification_wav(simulation, root / "sonification" / "coherence.wav")
            video_metadata = render_scene_mp4(scene, root / "sonification" / "coherence.wav", root / "video" / "preview.mp4")
        (root / "sonification" / "README.txt").write_text(
            "MIDI data-sonification cue. It maps Kuramoto order parameter to pitch and velocity. "
            "It is not a composed soundtrack and carries no claim about emotional response.\n",
            encoding="utf-8",
        )
        (root / "README.md").write_text(
            "# HAA-D-3 generated vertical slice\n\n"
            "Contents: source simulation, renderer-neutral SceneSpec, SVG frames, MP4 preview, WAV/MIDI sonification, "
            "MIDI/WAV data-sonification cue, MP4 preview and SHA-256 manifest.\n\n"
            "Status: GENERATED_NOT_REVIEWED. Numerical software checks do not establish empirical "
            "or biological validity. Human scientific, creative, accessibility and rights review "
            "is required before public release.\n",
            encoding="utf-8",
        )
        artifact_paths = sorted(path for path in root.rglob("*") if path.is_file())
        artifacts = {
            path.relative_to(root).as_posix(): {
                "sha256": _sha256(path),
                "size_bytes": path.stat().st_size,
            }
            for path in artifact_paths
        }
        release_basis = json.dumps(artifacts, sort_keys=True, separators=(",", ":")).encode("utf-8")
        manifest = {
            "release_id": hashlib.sha256(release_basis).hexdigest()[:20],
            "status": "GENERATED_NOT_REVIEWED",
            "evidence_class": "MODEL_OUTPUT",
            "source_model": simulation.get("model"),
            "parameters": simulation.get("parameters"),
            "scene_id": scene.get("scene_id"),
            "frame_count": len(list((root / "frames").glob("*.svg"))),
            "sonification": sonification,
            "wav_sonification": wav_metadata,
            "video": video_metadata,\n            "wav_sonification": wav_metadata,\n            "video": video_metadata,
            "artifacts": artifacts,
            "required_reviews": ["scientific", "creative", "accessibility", "rights"],
            "limitations": [
                "Generic Kuramoto oscillator model; not a biological brain model.",
                "MIDI is data sonification, not an original composed soundtrack.",
                "Generated artifacts have not undergone human review.",
            ],
        }
        (root / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        with zipfile.ZipFile(output_path, "w") as archive:
            for path in sorted(p for p in root.rglob("*") if p.is_file()):
                relative = path.relative_to(root).as_posix()
                info = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
    return output_path
