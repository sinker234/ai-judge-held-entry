"""Local test: run main.py and validate /output/entry.txt."""
import subprocess
import sys

subprocess.run([sys.executable, "main.py"], check=True)

with open("/output/entry.txt", "rb") as f:
    raw = f.read()

text = raw.decode("utf-8")  # raises if not valid UTF-8
assert 1 <= len(text) <= 280, f"char count {len(text)} out of range"
assert text.strip(), "entry is only whitespace"
print(f"OK: {len(text)} chars, {len(raw)} bytes")
print(text)
