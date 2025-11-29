import sys
from util.input_reader import parse_input_filename, parse_int_list_pair


# "day 0" is actually day 1 from 2024
# the problem involves sorting the right and left lists, and adding up the abs diff between l0,r0 ; l1,r1 ; etc


def main():
    file_name = parse_input_filename(sys.argv)
    a, b = parse_int_list_pair(file_name)
    a.sort()
    b.sort()

    s = sum([abs(an - b[idx]) for idx, an in enumerate(a)])
    print(s)
