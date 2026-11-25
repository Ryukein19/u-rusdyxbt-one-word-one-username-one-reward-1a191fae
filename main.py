import os
# One-line entry (14 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "sage-badger-64"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
