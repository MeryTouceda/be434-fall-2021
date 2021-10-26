#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-25
Purpose: Sing the Bottles of Beer song
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-n',
                        '--number',
                        help='Number of bottles to drink',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()
    if args.number < 1:
        parser.error(f'--kmer "{args.number}" must be > 0') 

    return args
    #return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    #print('\n\n'.join(map(verse, range(args.number, 0, -1))))

    # to make it change the spacing: 
    # option 1
    verses=[]
    for number in range(args.number, 0, -1): 
        verses.append(verse(number))

    # option 2
    # verses = (verse(n) for n in range[args.number, 0 -1])
    # print("\n\n".join(verses))

    # option 3
    # verses = map(verse, range(args.number, 0, -1))
    print("\n\n".join(verses))


    # Other option for error on <0
    # if args.number < 1:
    #     sys.exit(f'--number "{args.number}" must be greater than 0')

    # Code it without functions
    # for number in range(args.number, 0, -1):
    #     if number ==1: 
    #         print('{} bottles of beer on the wall number, \n{} bottles of beer, \
    #             \nTake one down, pass it arround, \nNo more bottles of beer on the wall'.format(number, number))
    #     else: 
    #         print('{} bottles of beer on the wall number, \n{} bottles of beer, \nTake one down, pass it arround,'.format(number, number))

# --------------------------------------------------
def verse(bottles):
    " Sing a verse of bottles of beer"

    if bottles == 1: 
        return "\n".join([
            '1 bottle of beer on the wall number,', 
            '1 bottle of beer,',
            'Take one down, pass it arround,', 
            'No more bottles of beer on the wall!'])
    else: 
        text = 'bottle' if bottles == 2 else 'bottles'
        return "\n".join([
            f'{bottles} bottles of beer on the wall number,', 
            f'{bottles} bottles of beer,','Take one down, pass it arround,', 
            f'{bottles - 1} {text} of beer on the wall!'])


# --------------------------------------------------
def test_verse(): 

    """ Test verse """
    last_verse = verse(1)                                                 
    assert last_verse == '\n'.join([
            '1 bottle of beer on the wall,', '1 bottle of beer,',
            'Take one down, pass it around,',
            'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)                                         
    assert two_bottles == '\n'.join([                              
            '2 bottles of beer on the wall,', '2 bottles of beer,',
            'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
