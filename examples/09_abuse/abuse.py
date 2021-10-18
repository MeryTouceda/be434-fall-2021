#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-18
Purpose: Rock the Casbah
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        metavar='insults',
                        type = int, 
                        help='Number of insults', 
                        default = 3)
    
    parser.add_argument('-a',
                        '--adjectives',
                        metavar='andjectives',
                        type = int, 
                        help='Random seed', 
                        default = 2)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default= None) #can leave this out but being splicit

    args = parser.parse_args()

    # make sure number and adjectives are over 0
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.strip().split() # make it a list

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.strip().split()

    print(random.choice(nouns))

    for _ in range(args.number): # _ I am not going to use the iterator
        adjs = ', '.join(random.sample(adjectives, k=args.adjectives))
        print(f'You {adjs} {random.choice(nouns)}!')



# --------------------------------------------------
if __name__ == '__main__':
    main()
