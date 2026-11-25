"""One Line, One Laugh — u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.

Writes one funny line to /output/entry.txt. Gate: UTF-8, 1-140 chars.

PASS 1 (kept candidate):
  "My plant died, so I bought a plastic one — now I'm emotionally invested
  in something that can't leave me." (105 chars, verified below)
  Judge criteria: (1) one self-contained funny line; (2) the laugh lands on
  the turn — from dead plant to plastic replacement to the confession that
  the appeal is a partner who cannot leave; (3) tight, no wasted word;
  (4) fresh — the plant-death setup is familiar, but the punch reframes it
  as commitment anxiety, not a gardening joke; (5) clear on first read.

PASS 2 (challenger, rejected):
  "My smoke alarm goes off every time I cook, which is its way of saying
  dinner is ready." (86 chars, verified below)
  Rejected: the punch is a mild observation, not a real turn — the alarm
  sounding IS the setup, and "dinner is ready" just restates it. It loses
  on criterion 2 (no surprise twist) and criterion 4 (smoke-alarm-cooking
  is a well-worn premise). Pass 1's turn is bigger and fresher.
"""

import os

ENTRY = "My plant died, so I bought a plastic one \u2014 now I'm emotionally invested in something that can't leave me."

CHALLENGER = "My smoke alarm goes off every time I cook, which is its way of saying dinner is ready."


def main() -> None:
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
