"""Deliver the 20 November 2026 world-news summary image.

The artwork ships in the repository as ``entry.png``. Running the
program copies it, byte for byte, to ``/output/entry.png`` after two
integrity checks: the PNG signature must be present and the SHA-256 of
the payload must match the digest recorded below. After writing, the
delivered file is read back and digest-checked again, so a short or
corrupted write fails loudly instead of shipping quietly. The output
is a pure function of the shipped file: repeated runs deliver
identical bytes.
"""

import hashlib
import os
import sys

EXPECTED_SHA256 = "0e0bee9d36ad7b1ea4e5784f8e1cac8e46f57179cd24996657dcdf1f46dade9d"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
TARGET_DIR = "/output"
TARGET = os.path.join(TARGET_DIR, "entry.png")


def find_source() -> str:
    """Locate the shipped entry.png from wherever the program runs."""
    candidates = []
    if "__file__" in globals():
        candidates.append(os.path.dirname(os.path.abspath(__file__)))
    if sys.argv and sys.argv[0]:
        candidates.append(os.path.dirname(os.path.abspath(sys.argv[0])))
    candidates.append(os.getcwd())
    for directory in candidates:
        path = os.path.join(directory, "entry.png")
        if os.path.isfile(path):
            return path
    raise SystemExit("entry.png not found beside the program")


def load_verified_payload() -> bytes:
    with open(find_source(), "rb") as handle:
        payload = handle.read()
    if not payload.startswith(PNG_SIGNATURE):
        raise SystemExit("entry.png is missing its PNG signature")
    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"entry.png digest mismatch: {digest}")
    return payload


def main() -> int:
    payload = load_verified_payload()
    os.makedirs(TARGET_DIR, exist_ok=True)
    with open(TARGET, "wb") as handle:
        handle.write(payload)
    with open(TARGET, "rb") as handle:
        delivered = handle.read()
    if hashlib.sha256(delivered).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("delivered file failed its post-write check")
    print(f"wrote {TARGET} ({len(delivered)} bytes, verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
