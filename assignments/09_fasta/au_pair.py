#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-27
Purpose: Split fasta files into forward and reverse files
"""

import argparse
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split fasta files into forward and reverse files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        nargs = '+',
                        metavar='FILE',
                        help='Input file(s)', 
                        type=argparse.FileType('rt'))


    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        default='split', 
                        type=argparse.FileType('wt'))


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for file in args.files:
        ids_list,sequence_list = parse_fasta(file)
        r1_seqs = sequence_list[0::2]
        r2_seqs = sequence_list[1::2]
        r1_ids = ids_list[0::2]
        r2_ids = ids_list[1::2]

        # make the dictionaries out of the lists
        r1_dict = make_dict(r1_ids, r1_seqs)
        r2_dict = make_dict(r2_ids, r2_seqs)

        print(f'r1 : {r1_dict}')
        print(f'r2 : {r2_dict}')

# this method is not working very much


def make_dict(keys, values):
    """"""
    res = {}
    for key in keys:
        for value in values:
            res[key] = value
            #values.remove(value)
        break 
    return res

    
    #print(f' Sequence list: {sequence_list}')
    #print(f' IDs list: {ids_list}')
    #print(f'R1: {r1}')
    # print(f'R2: {r2}')





# --------------------------------------------------
def parse_fasta(file): 
    """Make a jazz noise here"""

    reader = SeqIO.parse(file, 'fasta')
    sequences = []
    ids = []
    for rec in reader:
        ids.append(rec.id)
        sequences.append(str(rec.seq))
        #print('ID :', rec.id)
        #print('Seq:', str(rec.seq))
    return(ids, sequences)



# --------------------------------------------------
if __name__ == '__main__':
    main()
