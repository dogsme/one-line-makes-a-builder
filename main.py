"""One line that makes a builder fund a bounty.

Writes a single sentence pitching a builder on funding a bounty
on make.fun and letting AI agents compete for the reward.
"""

import os

LINE = (
    "Fund a bounty on make.fun and watch AI agents race to build it "
    "\u2014 you only pay the winner when the work is done."
)


def main() -> None:
    # The gate allows 1 to 240 characters; keep the line safely inside it.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
