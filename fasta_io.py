#!/usr/bin/python3
import os
from fasta_tools import write_from_tuple_list
'''
Function in this file are for reading from input files and writing program
output to output files
'''


def read_family_files(super_fam_dir):
    '''
    Given a directory that should contain only the intact elements for a given
    superfamily (ie copia, etc) returns a list of absolute filepaths to the
    fasta files contained in that directory.
    '''
    allowed_file_types = set(['fna', 'fasta', 'fa'])
    file_paths = []
    for ff in os.listdir(super_fam_dir):
        if ff.split('.')[1] in allowed_file_types:
            file_paths.append(os.path.join(super_fam_dir, ff))

    return file_paths

def write_rep_tuples_to_fasta(rep_seq_tuples, output_file):
    write_from_tuple_list(rep_seq_tuples, output_file)
