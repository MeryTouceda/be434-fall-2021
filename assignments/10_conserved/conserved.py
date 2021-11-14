#!/usr/bin/env python3
"""
Author : Mery Touceda-Suarez <mtoucedasuarez@email.arizona.edu>
         Ken Youens-Clark
Date   : 2021-11-08
Purpose: Find conserved bases
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sequences = args.file.read().split()

    if len(sequences) < 2:
        sys.exit("Input file must contain 2 or more sequences")

    alignment = create_alignment(sequences)
    print('\n'.join(sequences))
    print(alignment)


# --------------------------------------------------
def create_alignment(sequences):
    """ Makes alingment:
    takes: a file with multiple sequences
    returns: the character sequence of an alignment as a str
    (X) = no alignment
    (|) = alignment, identical bases in this position"""

    number_sequences = len(sequences)
    alignment = []

    for i in range(0, len(sequences[0])):
        combo = []
        for k in range(0, number_sequences):
            combo.append(sequences[k][i])
        if all(element == combo[0] for element in combo):
            alignment.append('|')
        else:
            alignment.append('X')
    # return(len(alignment))
    return ''.join(alignment)


# --------------------------------------------------
def test_create_alignment():
    """ Test """

    assert create_alignment(['A', 'A']) == '|'
    assert create_alignment(['A', 'B']) == 'X'
    assert create_alignment(['AA', 'AB']) == '|X'


# --------------------------------------------------
if __name__ == '__main__':
    main()
