#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-22
Purpose: Find common k-mers between two files
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common k-mers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    # make sure kmer size is greater than 0
    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Find common words between two files"""

    args = get_args()
    fh1 = args.file1
    fh2 = args.file2
    k = args.kmer

    # create dictionaries with kmer and occurrences in file
    # file 1
    words1 = count_kmers(fh1, k)
    # print(words1)

    # file 2
    words2 = count_kmers(fh2, k)
    # print(words2)

    # find shared
    shared = list(set(words1).intersection(words2))

    # print
    for kmer in shared:
        print('{:10} {:5} {:5}'.format(
            kmer, words1.get(kmer), words2.get(kmer)), end='\n')


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string
    takes:
    seq - sequence (word)
    k - kmer size
    returns: list of kmers in sequence """

    n = len(seq) - k + 1

    return [] if n < 1 else [seq[i:i + k] for i in range(n)]

# --------------------------------------------------


def count_kmers(fh, k):
    """ Count kmers in file and create a dictionary
    takes:
    fh - file handle of file in which we want to count kmers
    k - length of kmers
    returns: dictionary with kmers as keys and occurrence as values """

    words = {}
    for line in fh:
        for word in line.split():
            for kmer in find_kmers(word, k):
                if kmer in words:
                    words[kmer] += 1
                else:
                    words[kmer] = 1
    return words


# --------------------------------------------------
def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
