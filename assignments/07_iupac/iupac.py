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

    parser.add_argument('seq',
                        metavar='SEQ',
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
    sequence_list = args.seq

    # create the dictionary with the code
    iupac = {'A':'A', 'C':'C', 'G':'G', 'T':'T', 'U':'U', 
            'R':'AG', 'Y':'CT', 'S':'GC', 'W':'AT', 'K':'GT',
            'M':'AC', 'B':'CGT', 'D':'AGT', 'H':'ACT', 
            'V':'ACG', 'N': 'ACGT'}
    
    # for every sequence in the list of sequences provided
    for seq in sequence_list:
        output_seq = "" # initialize output sequence
        output_re = "" # initialize output regular expression

        # for every item (letter) in the sequence
        for item in seq: 
            # if the value in dictionary is more than one base
            if len(iupac.get(item)) > 1:
                #output_seq = output_seq + item
                # store the regular expression with brakets
                output_re = output_re + '[{}]'.format(iupac.get(item))
            else: 
                output_seq = output_seq + item
                output_re = output_re + iupac.get(item)
        
        print('{} {}'.format(seq, output_re), file = args.outfile)
    
    print('Done, see {}', format(args.outfile))

    


    

# --------------------------------------------------
if __name__ == '__main__':
    main()
