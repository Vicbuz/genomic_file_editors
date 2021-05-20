# genomic_file_editors
All python codes were used to edit my genomic data, file formats, filtering etc, in one way or another :

rename_samples_WGS.py

The rename_samples_WGS.py script is used to rename files after the directory they are in. Raw fasta files were sent with random names and the directory they were in was the sample name, with the suffix _1.fq.gz or _2.fq.gz . This was because the samples came with a name that was not easy to identify and had no sample number on but the directory did.
The python code was written for this problem. For example in file 6, contained my sample 6's sequences in forward (_1.fq.gz) and reverse (_2.fq.gz). 
 But the files were called things like E100011477_L1_B5RDAPIctfRAADAA-615_2.fq.gz this script changes that to 6.2.fq.gz.
 The script must be placed in the root directory that has all the sample directories in it.
 
 syntax is:
 
 rename_samples_WGS.py /path/to/sample/directories

CSV to PED - 
this script took a csv file that only had one base pair at monomorphic sites and typed out two as ped files must be biallelic. It also changed the data from long to wide format and placed a space inbetween each call. No call was changed form a blank to a 0, and the sample number was placed twice at the start. please note ped files also require map files that correspond to the order of the genotypes in the ped file. 

csv format recieved:

Sample Id	Sample Description	Call	Assay Id	Well Position	Description
1	 		437-ahb8451	A01	N.No-Alleles
1	 	G	312-ahb5635	A01	K.Non-Polymorphic
1	 		790-AMB-00632040	A01	N.No-Alleles
1	 	G	1035-AMB-00995347	A01	K.Non-Polymorphic
1	 		588-AMB-00228327	A01	N.No-Alleles

PED format:
1 1 0 0 0 -9 G G G G A G G G 0 0
6 6 0 0 0 -9 G G G G G G G G 0 0
11 11 0 0 0 -9 A G G G A G G A 0
