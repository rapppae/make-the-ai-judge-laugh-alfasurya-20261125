"""Entry for make.fun bounty "Make the AI Judge Laugh".

Entry text (draft v1): one funny line about office life.
Limit: 1 to 200 characters. No trailing newline is written.
"""

import os

ENTRY = "HR said dress for the job you want, so I showed up in pajamas — I want to work from bed."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
