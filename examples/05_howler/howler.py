#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-09-15
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type = str,
                        default = '')



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    if os.path.isfile(text): 
        if args.outfile: 
            out_fh = open(args.outfile,'wt')
            out_fh.write(open(text).read().upper() + '\n')
            out_fh.close()
        else:
            print("{}".format(open(text).read().upper()))
    else: 
        if args.outfile: 
            out_fh = open(args.outfile,'wt')
            out_fh.write(text.upper() + '\n')
            out_fh.close()
        else:
            print("{}".format(text).upper())

#  WHY DOESN'T THIS WORK???


# --------------------------------------------------
if __name__ == '__main__':
    main()


