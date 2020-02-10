'''
You can ignore this file, this was script parts that I used to seperate
and extract intact elements from the superfamily fasta files.
'''


import os
from fasta_tools import seperate_types_supfamily_wide
COPIA_PATH = '/media/ethan/EH_DATA/Soy_fams/Copia'
GYPSY_PATH = '/media/ethan/EH_DATA/Soy_fams/Gypsy'

def seperate_copia_elements():
    seperate_types_supfamily_wide(COPIA_PATH)



def pull_intacts(target_dir, output_dir, key='INTACT'):
    target_file_paths = [os.path.join(target_dir, target_file)
                         for target_file in os.listdir(target_dir) if key in target_file]
    for target_file in target_file_paths:
        cmd = 'cp {} {}'.format(target_file, output_dir)
        os.system(cmd)  # copy the file to the output dir
