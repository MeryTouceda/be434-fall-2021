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
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--output',
                        help='Output filename',
                        metavar='FILE',
                        type=str,
                        default='out.txt')
                                          
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    if os.path.isfile(args.output):
        out_fh = open(args.output, 'wt')
        out_fh.write()                              
        out_fh.close()
        print("Output written to {}".format(args.output))
    
    else: 
        print("Output wirtten to out.txt")
     



# --------------------------------------------------
if __name__ == '__main__':
    main()
