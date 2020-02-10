#!/usr/bin/python3
import os
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
