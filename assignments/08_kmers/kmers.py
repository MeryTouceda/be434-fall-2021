#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-22
Purpose: Find common k-mers between two files
"""

import argparse
import sys


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
    if args.kmer < 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')    
    
    return args


# --------------------------------------------------
def main():
    """Find common words between two files"""

    args = get_args()
    fh1 = args.file1
    fh2 = args.file2
    k = args.kmer

    def find_kmers(seq, k):
        """ Find k-mers in string """
        n = len(seq) - k + 1
        return [] if n < 1 else [seq[i:i + k] for i in range(n)]


    # for kmer in find_kmers(fh1.read(), k):
    #     print(kmer)
    #     # kmer_count1 = find_kmers(fh1.read().split(), k).count(kmer)
    #     # kmer_count2 = find_kmers(fh2.read().split(), k).count(kmer)
    #     # print(f'{kmer:10} {kmer_count1:5} {kmer_count2:5}')

    for line in args.file1:
        for word in line.split():
            for kmer in find_kmers(word, k):
                kmer_count1 = find_kmers(args.file1.split(), k).count(kmer) # NOTE: algo pasa aqui que no me esta encontrando bien los kmers para contarlos
                kmer_count2 = find_kmers(args.file2.split(), k).count(kmer)
                print(f'{kmer:10} {kmer_count1:5} {kmer_count2:5}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
