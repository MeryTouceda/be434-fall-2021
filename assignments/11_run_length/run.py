#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@email.arizona.edu>
Date   : 2021-11-12
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for seq in args.text.splitlines():
        print(rle(seq))


# --------------------------------------------------
def rle(seq: str) -> str:
    """ Create RLE """

    combined = []
    prev = ''
    count = 0

    for base in seq:
        if prev == '':
            prev = base
            count = 1
        elif base == prev:
            count += 1
        else:  # if base and previous are not same, move up one
            combined.append([prev, count])
            prev = base
            count = 1
    combined.append([prev, count])  # for the final set

    ret = ''
    for char, count in combined:
        ret += '{}{}'.format(char, count if count > 1 else '')

    return ret


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()
