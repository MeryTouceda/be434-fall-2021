#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-01
Purpose: Translate DNA/RNA to proteins
"""

import argparse
import os
#import sys
from pprint import pprint


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
                        required= True, 
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
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
    fh = args.codons
    out_fh = args.outfile
    
    # read codons into a dictionary
    codons = dict()
    for line in fh: 
        key, value = line.split()
        #key, value = line.rstrip().split()                         # this seems to do the same
        codons[key] = value
    #pprint(codons) # to check codons is created right

    # translate the sequence
    k = 3                                                           # set to desired kmer length
    proteinseq = list()                                             # initialize sequence to store the protein sequence
    for kmer in [seq[i:i + k] for i in range(0, len(seq), k)]:      # loop over kmers in sequence (sliding window = k)
        #print(kmer)                                                # to check for loop works
        proteinseq.append(codons.get(kmer.upper(),'-'))             # add value (AA) of kmer key (codon) to list

    # write output to file 
    out_fh.write(''.join(proteinseq))                              # write the contents of list as a string to file
    out_fh.close()
    print('Output written to "{}".'.format(out_fh.name))

# --------------------------------------------------
if __name__ == '__main__':
    main()
