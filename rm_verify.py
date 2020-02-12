#!/usr/bin/python3
import sys
import os
from args import get_args

from big_hitter import get_rep_sequences_from_family_files
from big_hitter import run_from_clstrs
from fasta_io import write_rep_tuples_to_fasta

from tblastn import convert_rep_seqs_to_longest_orf
from tblastn import run_tblastn

# would be good to add option to start the run from the clstr files
# so dont need to redo that everytime when testing


def main():
    run_args = get_args()
    rep_seqs = []
    if run_args.c:  # run from collection of clstr files
        rep_seqs = run_from_clstrs(run_args.c)
    else:  # run for the first time
        rep_seqs = get_rep_sequences_from_family_files(run_args.i, run_args.o)

    # declare output filepaths
    rep_fasta_file = os.path.join(run_args.o, 'rep_seqs.fa')
    tblastn_output_file = os.path.join(run_args.o, 'blast_results.csv')

    write_rep_tuples_to_fasta(rep_seqs, rep_fasta_file)
    # at this point rep seqs are written in a fasta file to the
    # output directory you specifed with -o arguement

    convert_rep_seqs_to_longest_orf(rep_fasta_file)
    # at this point req_seqs file as been overwritten with the longest
    # translated protein from all 6 open reading frames and should
    # be ready for tblastn
    print('Running blast')
    run_tblastn(blastdb=run_args.b, query=rep_fasta_file,
                outfile=tblastn_output_file, evalue=1e-150)



if __name__ == "__main__":
    main()
