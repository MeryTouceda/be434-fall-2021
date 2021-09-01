#!/usr/bin/env python3
"""
Author: Mery Touceda-Suarez <mtoucedasuarez@arizona.edu>
Purpose: Print a warning for having seen a certain thing, use the gramatically correct article ('a', 'an')
"""

import argparse

# ---------------------------------------------------------
def get_args(): 
    """ Get the command-line arguments """

    parser = argparse.ArgumentParser(description = 'Crow\'s Nest -- choose the correct article')
    parser.add_argument('word', metavar = 'word', help =  'A word')
    return parser.parse_args()

# ---------------------------------------------------------
def main(): 
    """ Make a jazz noise here """
    args = get_args()
    word = args.word

    # why doesn't this pass the consonant upper test?
    #if word[0].lower() in ['a','e','i','o','u']:   
    #    article = 'an'
    #else:
    #    article = 'a'

    # book option, does pass the consonant test
    article = 'an' if word[0].lower() in  'aeiou' else 'a'

    print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, word))


# ---------------------------------------------------------
if __name__ == '__main__':
    main()
