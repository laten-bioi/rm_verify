#!/usr/bin/python3
import sys
from args import get_args

from big_hitter import get_rep_sequences_from_family_files
from big_hitter import run_from_clstrs
from fasta_io import write_rep_tuples_to_fasta

# would be good to add option to start the run from the clstr files
# so dont need to redo that everytime when testing


def main():
    run_args = get_args()
    rep_seqs = []
    if run_args.c:  # run from collection of clstr files
        rep_seqs = run_from_clstrs(run_args.c)
    else:  # run for the first time
        rep_seqs = get_rep_sequences_from_family_files(run_args.i, run_args.o)

    rep_fasta_file = os.path.join(run_args.o, 'rep_seqs.fa')
    write_rep_tuples_to_fasta(rep_seqs, rep_fasta_file)

    # if reached this point means that we have the representative seqs
    # in a file. Now need to do the blasting from here

    # STEP 2: Run tblastx on all rep sequences
    # STEP 3: Count total hits (check redundant?)

    # STEP 4: Write some kind of output


if __name__ == "__main__":
    main()
