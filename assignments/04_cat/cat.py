#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-09-24
Purpose: Python implementation of the 'cat' function
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Get the arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true',
                        default='False')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.files:
        for line_num, line in enumerate(fh, start=1):
            if args.number is True:
                # print(line_num, line, sep='\t', end='')
                print("     {}\t{}".format(line_num, line), end='')
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
