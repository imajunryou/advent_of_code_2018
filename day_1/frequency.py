import argparse
import os


def parse_frequency(frequency):
    result = 0
    try:
        result = int(frequency)
    except ValueError:
        pass
    return result


def update_frequency(current_frequency, next_frequency):
    return current_frequency + next_frequency


def get_input_path():
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
    args = parser.parse_args()

    return os.path.join(args.path, args.file)


if __name__ == "__main__":
    current_frequency = 0
    with open(get_input_path(), 'r') as f:
        for next_frequency in f:
            current_frequency = update_frequency(
                current_frequency,
                parse_frequency(next_frequency)
            )
    print(current_frequency)
