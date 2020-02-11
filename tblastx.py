import subprocess

'''
tblastx command template and args to use

-outfmt 10  # comma seperated values
-evalue threshold for saving hits
-html produce html output could be good for visualization
-num threads sets threads to use

tblastx -db [database name] -query [input file name]
-out outfile name
'''


def run_tblastx(blastdb, query, evalue=10, threads=1, outfmt=10):
    # outfmt 10 for comma seperated file
    cmd = ['tblastx', '-query', query, '-db', blastdb, '-evalue', evalue,
           '-num_threads' threads, '-outfmt', 10]
    # command still needs testing
    call = subprocess.call(cmd, shell=True)

    return call


def count_tblastx_hits(tblastx_output):
    pass
