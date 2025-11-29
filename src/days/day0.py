import sys
from util.input_reader import read_input


def main():
    param = sys.argv[1]
    print(f"day 0 main, run with '{param}'")
    infile = read_input(param)
    print(infile)
