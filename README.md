# genomic_file_editors
python codes used to edit my genomic data and files

rename_samples_WGS.py

The rename_samples_WGS.py script is used to rename files after the directory they are in. Raw fasta files were sent with random names and the directory they were in was the sample name, with the suffix _1.fq.gz or _2.fq.gz . This was because the samples came with a name that was not easy to identify and had no sample number on but the directory did.
The python code was written for this problem. For example in file 6, contained my sample 6's sequences in forward (_1.fq.gz) and reverse (_2.fq.gz). 
 But the files were called things like E100011477_L1_B5RDAPIctfRAADAA-615_2.fq.gz this script changes that to 6.2.fq.gz.
 The script must be placed in the root directory that has all the sample directories in it.
 
 syntax is:
 
 rename_samples_WGS.py /path/to/sample/directories
