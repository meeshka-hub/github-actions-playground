#!/usr/bin/env python3
import os
import random
import sys

SYMBOLS = ["🍒", "🍋", "🔔", "⭐", "💎", "7️⃣"]
WEIGHTS = [57, 25, 10, 5, 2, 1]


def pick_symbol() -> str:
    roll = random.randint(0, 99)
    threshold = 0

    for symbol, weight in zip(SYMBOLS, WEIGHTS):
        threshold += weight
        if roll < threshold:
            return symbol

    return SYMBOLS[-1]


def main() -> int:
    symbol = pick_symbol()
    print(f"🎰 Rolled: {symbol}")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as handle:
            handle.write(f"symbol={symbol}\n")

    print(f"symbol={symbol}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
