import argparse
import os
import sys
import profile
from typing import List, Tuple

from oset import oset

def parse_frequency(frequency):
    result = 0
    try:
        result = int(frequency)
    except ValueError:
        pass
    return result


def update_frequency(frequency: 'oset', next_frequency: int) -> 'Tuple[oset, int]':
    most_recent_frequency = frequency[-1]
    subtotal = most_recent_frequency+next_frequency
    frequency.add(subtotal)
    return (frequency, subtotal)


def get_args(args):
    parser = argparse.ArgumentParser(
        description=(
            "Tabulate frequencies from an input file.  "
            "Puzzle 1 from Advent of Code 2018."
        )
    )
    parser.add_argument(
        "--path", default=".", help=(
            "The path to the file with the desired frequency "
            "updates.  Defaults to the current directory."
        )
    )
    parser.add_argument(
        "--file", default="frequencies.txt", help=(
            "The name of the file with the desired frequency "
            "updates.  Defaults to \"frequencies.txt\""
        )
    )
    parser.add_argument(
        "--initial", default=0, type=int, help=(
            "The initial starting frequency.  Defaults to 0."
        )
    )
    parser.add_argument(
        "--repeat", action="store_true", help=(
            "Aborts frequency updating and reports the most recent sum "
            "after encountering the same subtotal twice."
        )
    )
    return parser.parse_args(args)


def get_input_path(args):
    return os.path.join(args.path, args.file)


def find_repeat(current_frequency: 'oset', frequencies: 'List[int]') -> int:
    looping = True
    subtotal = current_frequency[-1]  # type: ignore  # subtotal is an int
    loops = 0
    while looping:
        loops += 1
        for next_frequency in frequencies:
            previous_size = len(current_frequency)
            current_frequency, subtotal = update_frequency(current_frequency, next_frequency)
            if previous_size == len(current_frequency):
                print("Duplicate found")
                looping = False
                break
        print("."*loops)
    return subtotal


if __name__ == "__main__":
    args = get_args(sys.argv[1:])
    subtotal = args.initial
    current_frequency = oset([subtotal])
    with open(get_input_path(args), 'r') as f:
        frequencies = [parse_frequency(next_frequency) for next_frequency in f]
        if args.repeat == True:
            print("Hunting for repeats")
            subtotal = find_repeat(current_frequency, frequencies)
        else:
            print("Finding a sum")
            subtotal = sum(frequencies)
    print(subtotal)

