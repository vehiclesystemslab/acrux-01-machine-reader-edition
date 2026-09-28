#!/usr/bin/env python3
"""Verify the immutable ACRUX-01 Forensic Freeze release asset without decoding it."""
from __future__ import annotations
import hashlib
import pathlib
import subprocess
import sys
import tempfile
import zipfile

EXPECTED = "C54C0247BF9A6BF0BFBFF9CE990E9311171C3C9073F5E0EDD7A6A4EB8EB4D170"

def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_release.py ACRUX01_FORENSIC_FREEZE_G1_G12_v1.0.0.zip")
        return 2
    src = pathlib.Path(sys.argv[1]).resolve()
    if not src.is_file():
        print(f"ERROR missing file: {src}")
        return 2
    actual = sha256(src)
    print(f"expected_sha256={EXPECTED}")
    print(f"actual_sha256={actual}")
    if actual != EXPECTED:
        print("FAIL_OUTER_SHA256")
        return 1
    with tempfile.TemporaryDirectory(prefix="acrux01-freeze-") as td:
        root = pathlib.Path(td)
        with zipfile.ZipFile(src) as zf:
            bad = zf.testzip()
            if bad is not None:
                print(f"FAIL_ZIP_INTEGRITY={bad}")
                return 1
            zf.extractall(root)
        candidates = list(root.rglob("verify_freeze.py"))
        if not candidates:
            print("PASS_OUTER_SHA256_AND_ZIP")
            print("NOTE embedded verify_freeze.py not found; outer artifact remains hash-verified")
            return 0
        proc = subprocess.run([sys.executable, str(candidates[0])], cwd=candidates[0].parent)
        if proc.returncode != 0:
            return proc.returncode
    print("PASS_ACRUX01_GITHUB_RELEASE_VERIFY")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
