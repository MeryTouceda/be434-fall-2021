#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-09-15
Purpose: Jump the 5 but arguments on command line don't need to be a string
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        nargs = '+', 
                        help='Input text')

 
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {'1':'9','2':'8','3':'7','4':'6','5':'0','6':'4','7':'3','8':'2','9':'1'} # create a dictionary

    for word in args.text: 
        for char in word:
            print(jumper.get(char,char), end = '')
        print('')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
