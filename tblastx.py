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
