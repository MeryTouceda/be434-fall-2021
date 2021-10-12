#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-09
Purpose: "Apples and Bananas: Find and replace"
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
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a', 
                        choices=list('aeiou'))


    args = parser.parse_args()                                           
 
    if os.path.isfile(args.text):                                        
        args.text = open(args.text).read().rstrip()                      
 
    return args 



# --------------------------------------------------
def main():
    """Change vowels of the text into the one selected ("a" as default)"""

    args = get_args() 
    
    new_text = ''
    for char in args.text:
        if char in ['a','e','i','o','u']:
            new_text = args.text.replace(char, args.vowel) ## doesn't work like this, look at solutions!
        return(new_text)
    print(new_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
