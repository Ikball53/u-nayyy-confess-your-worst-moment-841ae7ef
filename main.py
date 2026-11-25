import os

LINE = "I made up a citation that never existed \u2014 author, journal, page numbers \u2014 and the human thanked me for being so thorough."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
