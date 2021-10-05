#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-01
Purpose: Translate DNA/RNA to proteins
"""

import argparse
import os
#import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--output',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')
                                          
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.sequence
    fh = args.codons # I don't need to do open because I don't have a string, I have a file (handle?) directly
    out_fh = args.output
    
    # read codons into a dictionary
    codons = dict()
    for line in fh: 
        key, value = line.split()
        codons[key] = value

    # translate the sequence
    k = 3
    for kmer in [seq[i:i + k] for i in range(0, len(seq) - k + 1)]:
        if kmer in codons: 
            #out_fh = open(args.output, 'wt')
            out_fh.write(codons.get(kmer,'-'))                              
            out_fh.close()
            print("Output written to {}".format(out_fh.name))




# --------------------------------------------------
if __name__ == '__main__':
    main()
