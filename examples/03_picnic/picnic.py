#!/usr/bin/env python3
"""
Author: Mery Touceda-Suarez <mtoucedasuarez@arizona.edu>
Purpose: List picnic foods
"""

import argparse

# ---------------------------------------------------------
def get_args(): 
    """ Get the command-line arguments """

    parser = argparse.ArgumentParser(description = 'Crow\'s Nest -- choose the correct article')
    parser.add_argument()
    return parser.parse_args()

# ---------------------------------------------------------
def main(): 
    """ Make a jazz noise here """
    args = get_args()


# ---------------------------------------------------------
if __name__ == '__main__':
    main()
