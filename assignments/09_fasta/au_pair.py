#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-10-27
Purpose: Split fasta files into forward and reverse files
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split fasta files into forward and reverse files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        nargs='+',
                        metavar='FILE',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        default='split',
                        type=str)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Split fasta into forward and reverse reads.
    Create two files in the output directory where those reads
    will be stored.
    """

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for file in args.files:
        basename = os.path.basename(file.name)
        root, ext = os.path.splitext(basename)
        with open(os.path.join(out_dir, root + '_1' + ext),
                  "wt", encoding='utf-8') as f_outfile:
            with open(os.path.join(out_dir, root + '_2' + ext),
                      "wt", encoding='utf-8') as r_outfile:
                for i, record in enumerate(SeqIO.parse(file, 'fasta')):
                    # alternative line for all the following (if statement) + is_even function
                    #SeqIO.write(record, f_outfile if is_even() else r_outfile, "fasta")
                    if i % 2 == 0:
                        # print(f'Odd : {record.id} \n {record.seq}')
                        f_outfile.write(str(">" + record.id + '\n'))
                        f_outfile.write(str(record.seq + '\n'))
                    else:
                        # print(f'Even : {record.id} \n {record.seq}')
                        r_outfile.write(str(">" + record.id + '\n'))
                        r_outfile.write(str(record.seq + '\n'))
    print(f'Done, see output in "{out_dir}"')


# # --------------------------------------------------
# def is_even(num):
#     # Return True if number is even

#     return num % 2 == 0


# --------------------------------------------------
if __name__ == '__main__':
    main()
