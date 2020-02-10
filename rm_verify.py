#!/usr/bin/python3
import sys
from args import get_args
from big_hitter import get_rep_sequences_from_family_files

def main():
    run_args = get_args()
    rep_seqs = []
    try:
        rep_seqs = get_rep_sequences_from_family_files(run_args.i, run_args.o)
    except (FileNotFoundError, IsADirectoryError) as e:
        print('Threw the following errors')
        for error in e:
            print(str(error))
        sys.exit(1)

    # if reached this point means that we have the representative seqs
    # in a list of tuples. Now need to do the blasting from here

    # STEP 2: Run tblastx on all rep sequences
    # STEP 3: Count total hits (check redundant?)

    # STEP 4: Write some kind of output
