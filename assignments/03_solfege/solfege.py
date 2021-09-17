#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-09-17
Purpose: The Sound of Music
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tell me the lyrics to the Sound of Music',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        nargs='+',
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    sound = {'Do': 'A deer, a female deer',
                'Re': 'A drop of golden sun',
                'Mi': 'A name I call myself',
                'Fa': 'A long long way to run',
                'Sol': 'A needle pulling thread',
                'La': 'A note to follow sol',
                'Ti': 'A drink with jam and bread'}

    for word in text:
        if word in sound:
            print('{}, {}'.format(word, sound.get(word)))
        else:
            print("I don't know \"{}\"".format(word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
