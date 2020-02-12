# rm_verify
Pipeline to verify repeat masker results on incomplete assemblies. 

Some functions use stuff that is included in [fasta_tools](https://github.com/EthanHolleman/fasta_tools) repository.  
To make sure everything works you can install the repo using pip with the command below. 

```
pip install git+https://github.com/EthanHolleman/fasta_tools
```

To uninstall use  
```
pip uninstall fasta_tools
```
You also need to install cd-hit, use the command below.
```
sudo apt-get install cd-hit
```
# Current State

As of now you should be able to download the clustered files from the lab drive and run the tblastn search with a command that looks like the one below.
```
python3 rm_verify.py -c You/path/to/cluster/files -o your/output/directory/path -b /your/path/to/blast/database
```
I haven't run the tblastn all the way through since seems like it is going to take a bit to complete. Will try and run it on the server sometime tommorow. 
