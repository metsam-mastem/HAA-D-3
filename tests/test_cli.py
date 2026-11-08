import tempfile
import unittest
from pathlib import Path

from haa_d3.cli import _read_json


class CliJsonInputTests(unittest.TestCase):
    def test_rejects_duplicate_object_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"schema_version":"0.1","schema_version":"0.2"}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON object key"):
                _read_json(path)

    def test_rejects_non_standard_nan_and_infinity_constants(self):
        for token in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(token=token), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "non-standard.json"
                path.write_text('{"value":' + token + '}', encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "non-standard JSON numeric constant"):
                    _read_json(path)

    def test_reads_valid_json_objects(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.json"
            path.write_text('{"schema_version":"0.1","title":"safe"}', encoding="utf-8")
            self.assertEqual(_read_json(path), {"schema_version":"0.1","title":"safe"})


    def test_rejects_json_files_over_input_size_budget(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "oversized.json"
            with path.open("wb") as stream:
                stream.truncate(16 * 1024 * 1024 + 1)
            with self.assertRaisesRegex(ValueError, "file size limit"):
                _read_json(path)


if __name__ == "__main__":
    unittest.main()
