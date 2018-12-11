import argparse
import os
import sys


def parse_frequency(frequency):
    result = 0
    try:
        result = int(frequency)
    except ValueError:
        pass
    return result


def update_frequency(current_frequency, next_frequency):
    return current_frequency + next_frequency


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
    return parser.parse_args(args)


def get_input_path(args):
    return os.path.join(args.path, args.file)


if __name__ == "__main__":
    args = get_args(sys.argv[1:])
    current_frequency = args.initial
    with open(get_input_path(args), 'r') as f:
        for next_frequency in f:
            current_frequency = update_frequency(
                current_frequency,
                parse_frequency(next_frequency)
            )
    print(current_frequency)
