"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet, concrete scene
written to relax the reader. Python 3.13, stdlib only, deterministic,
no network.
"""

import os

TEXT = (
    "The kettle has gone quiet. Evening light comes in low across the table "
    "and stays there, amber on the wood, not asking anything. Somewhere a "
    "clock ticks the way a heart does when nobody is listening. The room "
    "lets out a long breath, and the light stays where it fell."
)


def main() -> None:
    # Guard the sealed scorer's gate: 1-280 Unicode code points, not
    # whitespace-only. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit(
            f"entry text invalid: {len(TEXT)} chars, "
            f"whitespace-only={not TEXT.strip()}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
