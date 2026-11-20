"""Deliver the 20 November 2026 world-news summary image.

The artwork ships beside this program as ``entry.png``. Running the
program copies it, byte for byte, to ``/output/entry.png`` after two
integrity checks: the PNG signature must be present and the SHA-256 of
the payload must match the digest recorded below. The output is a pure
function of the shipped file, so repeated runs produce identical bytes.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET_DIR = "/output"
TARGET = os.path.join(TARGET_DIR, "entry.png")

EXPECTED_SHA256 = "0e0bee9d36ad7b1ea4e5784f8e1cac8e46f57179cd24996657dcdf1f46dade9d"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def load_verified_payload() -> bytes:
    with open(SOURCE, "rb") as handle:
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
    print(f"wrote {TARGET} ({len(payload)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
