#!/usr/bin/python3
'''
This file contains functions relating to the use of cd-hit for family based
clustering. Starting with a dir with the intact elements of each family in
sepetate files using the functions in this file one can extract the header
and sequence of the representative seq of the largest cluster for each family

See get_rep_sequences_from_family_files() function
'''

import subprocess
import os

from fasta_io import read_family_files
from fasta_tools import read_as_tuples


def run_cd_hit(output, input_file, identity=0.90):
    '''
    Given an oputput file path and input_file path runs cd-hit-est on the
    input file and writes the .clstr file to the output file. Sorts the clstr
    file by clstr size which is currently required for get_largest_cluster_rep
    function to work correctly.
    '''
    cmd = ['cd-hit-est', '-i', input_file, '-o', output,
           '-c', str(identity), '-d', '0', '-sc', '1']

    FNULL = open(os.devnull, 'w')  # prevent cd-hit from writing studd to
    # the command line; just cleans things up does not effect the output
    try:
        hit = subprocess.call(cmd, stdout=FNULL, stderr=subprocess.STDOUT)
        # print(cmd)
        # os.system(cmd)
    except subprocess.CalledProcessError as e:
        return e
    # cd hit for a single file


def cluster_superfamily_files(super_fam_paths, output_dir):
    '''
    Given a list of intact family elements paths run cd hit on each file
    and write the output to the output_dir. A list of family files can be
    obtained from the read_family_files function in io.py
    '''
    file_map, l = {}, len(super_fam_paths)
    for i, family_file in enumerate(super_fam_paths):
        output_file = os.path.join(
            output_dir, os.path.basename(family_file).split('.')[0])
        # take just the basename of the family file path, remove the fasta
        # file extension and join it with the output file dir to give a complete
        # outoput file path with no extension. cd-hit then auto adds the .clstr
        # extension onto the output file name given by -o
        print('Clustering {} of {}'.format(i+1, l))
        run_cd_hit(output_file, family_file)
        file_map[family_file] = output_file + '.clstr'

    return file_map
    # return a dictionary where key = clstr file and value is the path
    # to the fasta file that cd hit was called on to produce the clstr file


def get_largest_cluster_rep(clstr_file, assume_sorted=True, rep_identifier='*'):
    '''
    Given a path to a clstr file returns the representative sequence of the
    largest cluster in the file. Currently assumes the clstr file is sorted so
    largest cluster is the first in the file. This behavior is set using the
    -sc 1 paramter in the run_cd_hit function.
    '''
    with open(clstr_file) as cf:
        while cf:
            line = cf.readline().strip()
            if line[-1] == rep_identifier:
                return line
        return False


def format_rep_header(rep_header):
    '''
    Given the representative sequence line from a clstr file, returns just the
    name of that sequence as it appears in the original fasta file. Used to
    match the rep seq back to the original fasta.
    Rep seq in the clstr file looks like below

    2	9432nt, >name=RLC_Gmr2_Gm1-29... *

    '''
    return rep_header.split(', ')[1][:-5]


def get_rep_sequence(fasta_file_path, clstr_file_path):
    '''
    Given a path to a fasta file and the clstr file produced by cd hit for the
    fasta file returns the header and sequence of the representative sequence
    identified by cd-hit as a tuple.
    '''
    fasta_files = read_as_tuples(fasta_file_path)
    target = format_rep_header(get_largest_cluster_rep(clstr_file_path))
    # pulls out a name that looks like >name=RLC_Gmr2_Gm1-29 which will be
    # the first thing in the header of the seq in the fasta file we want to
    # match to
    for header, seq in fasta_files:
        name = header.split(' ')[0]
        # gives just the name of the element
        # assuming standard soybase fasta header format
        if name == target:
            return header, seq
    return False  # no match found uh oh :(


def get_rep_sequences_from_family_files(superfam_dir, output_dir):
    '''
    This function brings all the above functions together. Given a directory
    with the intact elements from one superfamily seperated by family returns
    the representative sequences from the largest cluster within each family as
    a list of tuples. tuple[0] = the rep seq header tuple[1] = rep seq sequence
    '''
    rep_seq_list = []
    family_file_paths = read_family_files(superfam_dir)
    cluster_file_map = cluster_superfamily_files(family_file_paths, output_dir)
    for family_file, clstr_file in cluster_file_map.items():
        rep_seq_list.append(get_rep_sequence(family_file, clstr_file))

    return rep_seq_list

# example call
#a = get_rep_sequences_from_family_files('/home/ethan/Documents/Copia_Intacts_Test',
#                      '/home/ethan/Documents/pipe_test')
