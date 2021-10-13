#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-08
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh1 = args.file1
    fh2 = args.file2
    output_file = args.outfile

    # convert files into list of words
    file1 = fh1.read().split()
    file2 = fh2.read().split()

    # find the shared words between the two lists
    shared = sorted(list(set(file1).intersection(file2)))

    # print out to output file or STDIN
    if output_file:
        output_file.write('\n'.join(shared))
        output_file.close()
    else:
        print('\n'.join(shared))


# --------------------------------------------------
if __name__ == '__main__':
    main()
