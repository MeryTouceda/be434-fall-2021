#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@email.arizona.edu>
Date   : 2021-11-21
Purpose: Python grep
"""

import argparse
import sys
import re
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('PATTERN',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('FILE',
                        nargs = '*',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'))
    
    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true',
                        default=False)
    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output)',
                        metavar='FILE',
                        type=argparse.FileType('wt'), 
                        default=sys.stdout)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.FILE:
        if args.outfile != sys.stdout:
            #args.outfile.write('{}:'.format(fh.name) if len(args.FILE) > 1 else None)
            for line in fh:
                search = re.search(args.PATTERN, line, re.I) if args.insensitive else re.search(args.PATTERN, line) 
                if search:
                    args.outfile.write(line)


        else:  # no outfile
            print('{}:'.format(fh.name)) if len(args.FILE) > 1 else None
            for line in fh:
                search = re.search(args.PATTERN, line, re.I) if args.insensitive else re.search(args.PATTERN, line) 
                if search:
                    print(line, end ="")


    

# --------------------------------------------------
if __name__ == '__main__':
    main()
