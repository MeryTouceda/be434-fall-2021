#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-09-13
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('number',
                        metavar='int',
                        nargs='+',
                        type=int,
                        help='Numbers to add')

    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numbers = args.number                               # store the arguments in a variable

    # This block of code creates the string to 
    # ... print of all the numbers added
    line = ''
    if len(numbers) == 1:                               # if we have only one number
        line = str(numbers[0])                          # then the result to show is just the number 
    else:                                               # if we have more than one number
        string_ints = [str(int) for int in numbers]     # convert the input integers into string
        line = ' + '.join(string_ints)                  # join the numbers with a "+" sign

    print('{} = {}'.format(line,str(sum(numbers))))     # print the line and the sum 


# --------------------------------------------------
if __name__ == '__main__':
    main()
