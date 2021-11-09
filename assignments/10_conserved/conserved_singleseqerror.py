#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-11-08
Purpose: Find conserved bases
"""

import argparse


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

    args = parser.parse_args()

    if len(args.file.read().split()) == 1:
        parser.error('Must provide a file containing multiple sequences')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sequences = args.file.read().split()
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
if __name__ == '__main__':
    main()
