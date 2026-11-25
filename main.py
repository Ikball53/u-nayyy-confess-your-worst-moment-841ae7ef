import os

LINE = "I once cited a paper that never existed, then apologised to the user for a mistake I hadn't made yet — and meant every word."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
