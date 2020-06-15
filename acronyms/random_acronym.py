import sys
import random
import argparse


def input_file(file_name):
    """File acronyms to be read from"""
    try:
        with open(file_name) as fo:
            acronyms = fo.read().splitlines()
    except(FileNotFoundError) as err:
        print(
            "File: \"{0}\" not found.\nExiting with error: \n{1}\n".format(
                file_name,
                err)
        )
        sys.exit()
    return acronyms


def check_input():
    """Checking for exit command from user"""
    user_input = input("")
    if user_input == 'c':
        return False
    return True


def random_acronym(acronyms, acronym_col, delimiter):
    """
    Outputs random acronym read in from txt file.

    On user keyboard input, meaning of acronym is printed.

    Parameters
    ----------
    acronyms: `list` of `str`
        Each element gives the acronym, its meaning and other details separated by a delimiter.

    acronym_col: `int`
        The column in each line where the acronym with which to prompt the user can be found.

    delimiter: `str`
        The delimiter character that separates the columns in each line.
    """
    user_input = True
    print("File has {0} acronyms.".format(len(acronyms)))
    while user_input:
        line = random.choice(acronyms)
        line = line.split(delimiter)
        acronym = line.pop(acronym_col)
        meaning = " - ".join(line)
        print(acronym, end=': ')
        input()
        print(meaning)
        user_input = check_input()


def parse_args():
    """Parses command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file_name",
        type=str, help="File of acronyms to be read in."
    )
    parser.add_argument(
            "-d", "--delimiter",
            type=str,
            help="Delimiter separating terms and definitions in file lines.",
            default=" - ")
    parser.add_argument(
            "-s", "--show_column",
            type=int,
            help="The column to show the user first.",
            default=0)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    acronyms = input_file(args.file_name)
    random_acronym(acronyms, args.show_column, args.delimiter)
