#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-13
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('SEQ',
                        metavar='str',
                        nargs= '+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sequence_list = args.SEQ

    # create the dictionary with the code
    iupac = {'A':'A', 'C':'C', 'G':'G', 'T':'T', 'U':'U', 
            'R':'AG', 'Y':'CT', 'S':'GC', 'W':'AT', 'K':'GT',
            'M':'AC', 'B':'CGT', 'D':'AGT', 'H':'ACT', 
            'V':'ACG', 'N': 'ACGT'}
    
    for seq in sequence_list: 
        for item in seq: 
            if len(iupac.get(item)) > 1:
                print('{} [{}]'.format(item, iupac.get(item)))
            else: 
                print('{} {}'.format(item, iupac.get(item))) 



  



# --------------------------------------------------
if __name__ == '__main__':
    main()
