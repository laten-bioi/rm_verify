import subprocess
from Bio.Seq import Seq
from Bio import SeqIO
from fasta_tools import read_as_tuples

'''
tblastn command template and args to use

-outfmt 10  # comma seperated values
-evalue threshold for saving hits
-html produce html output could be good for visualization
-num threads sets threads to use

tblastx -db [database name] -query [input file name]
-out outfile name
'''


def run_tblastn(blastdb, query, evalue=10, threads=1, outfmt=10):
    # outfmt 10 for comma seperated file
    cmd = ['tblastn', '-query', query, '-db', blastdb, '-evalue', evalue,
           '-num_threads', threads, '-outfmt', 10]
    # command still needs testing
    call = subprocess.call(cmd, shell=True)

    return call


def count_tblastx_hits(tblastx_output):
    pass


def six_frames(seq):
    '''
    Given a seq string converts into sixe possible reading frames and translates
    frames into protein sequences. Returns as a list.
    '''
    rc = str(Seq(seq).reverse_complement())

    def three_frames(s):
        return [s, s[1:-2], s[2:-1]]
    frames = three_frames(seq) + three_frames(rc)
    return [str(Seq(f).translate()) for f in frames]


def find_longest_orfs(frames, stop_symbol='*', start_codon='M'):
    '''
    Given a list of potential open reading frames from six_frames returns the
    max length open reading frame from that list by looking for the first start
    codon in the potential reading frame (porf).
    '''
    orfs = []
    for f in frames:
        f = f.split('*')
        for porf in f:
            for i, nucl in enumerate(porf):
                if nucl == start_codon:
                    orfs.append(porf[i:])

    return max(orfs, key=lambda x: len(x))


def convert_rep_seqs_to_longest_orf(rep_seq_fasta):
    '''
    Given a fasta file of sequnces (should be the rep sequences) returns a list
    of tuples where first item is the oringal header and second is the longest
    ORF found in that header's sequence. Can then be passed off to the tblastn
    search method.
    '''
    rep_proteins = []

    for rep_header, rep_seq in read_as_tuples(rep_seq_fasta):
        rep_proteins.append((rep_header,
                            find_longest_orfs(six_frames(rep_seq))))

    return rep_proteins  # returns as a list of tuples
    # original header with the longest orf



#quick tests TODO: Delete this
#f = '/home/ethan/Documents/Gypsy/Gmr1INTACT.fna'
#convert_rep_seqs_to_longest_orf(f)
