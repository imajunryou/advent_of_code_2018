import argparse
import os
import sys
from collections import Counter
from typing import List, Tuple


def has_n(word: str, n: int) -> bool:
    frequencies = Counter(word)
    return n in frequencies.values()

def has_two(word: str) -> bool:
    return has_n(word, 2)

def has_three(word: str) -> bool:
    return has_n(word, 3)

def has_counts(word: str) -> Tuple[bool, bool]:
    return (has_n(word, 2), has_n(word, 3))

def total_counts(words: List[str]) -> Tuple[int, int]:
    x, y = 0, 0
    for word in words:
        counts = has_counts(word)
        x += 1 if counts[0] else 0
        y += 1 if counts[1] else 0
    return (x, y)

def get_args(args):
    parser = argparse.ArgumentParser(
        description=(
            "Find the checksum from a list of box IDs "
            "consisting of lower-alphabet string.  The "
            "checksum consists of the product of the "
            "counts of double- and triple-occurences of "
            "letters in the IDs."
        )
    )

    parser.add_argument(
        "--path", default=".", help=(
            "The path to the file containing the desired IDs"
        )
    )

    parser.add_argument(
        "--file", default="ids.txt", help=(
            "The name of the file containing the desired IDs"
        )
    )

    return parser.parse_args(args)

if __name__ == "__main__":
    args = get_args(sys.argv[1:])
    with open(os.path.join(args.path, args.file), 'r') as f:
        ids = f.readlines()
        counts = total_counts(ids)
        print(counts[0] * counts[1])
