#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-09-13
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

                        
    parser.add_argument('-s', '--sorted',
                        help='Sort the items',
                        action = 'store_true') 
              

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item   
    
    if args.sorted: 
        items.sort()                                     

    bringing = '' #initialize an empty string to store the modified list
    if len(items) == 1: 
        bringing = items[0]
    elif len(items) == 2:
        bringing = ' and '.join(items)
    else: 
        items[-1] = 'and ' + items[-1] 
        bringing = ', '.join(items) 
        

    print(" You are bringing {}.".format(bringing))

   


# --------------------------------------------------
if __name__ == '__main__':
    main()
