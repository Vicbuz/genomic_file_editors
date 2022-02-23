# genomic_file_editors
All python codes were used to edit my genomic data, file formats, filtering etc, in one way or another :

## RENAME SAMPLES rename_samples_WGS.py

This script is used to rename files after the directory they are in. 
Raw fasta files were sent with random names and the directory they were in was the sample name, with the suffix _1.fq.gz or _2.fq.gz. This was because the samples came with a name that was not easy to identify and had no sample number on but the directory did. For example in file 6, contained sample 6's sequences for the forward (_1.fq.gz) and reverse (_2.fq.gz) reads. But the files were called things like E100011477_L1_B5RDAPIctfRAADAA-615_2.fq.gz this script changes that to 6.2.fq.gz. The script must be placed in the root directory that has all the sample directories in it.

 
 syntax is:
 
 rename_samples_WGS.py /path/to/sample/directories

## CSV TO PED  csv_to_ped.py

This script took a csv formatted file resulting from a SNP array run and changed it to ped and map, plink formatted files. That csv had one base pair at monomorphic sites and typed out two as ped files must be biallelic. This code also changed the data from long to wide format and placed a space in-between each base call. If there was no call in the csv a ‘0’ was recorded. Additionally, the sample number was placed twice at the start. Please note ped files also require map file that contains the chromosome and position of each SNP that correspond to the order of the SNPs in the ped file.

csv format recieved:

Sample Id,	Sample Description,	Call,	Assay Id,	Well Position,	Description

1,	 		,437-ahb8451,	A01,	N.No-Alleles

1,	 	G,	312-ahb5635,	A01,	K.Non-Polymorphic

1,	 		,790-AMB-00632040,	A01,	N.No-Alleles

1,	 	G,	1035-AMB-00995347,	A01,	K.Non-Polymorphic


PED format:

1 1 0 0 0 -9 G G G G A G G G 0 0

6 6 0 0 0 -9 G G G G G G G G 0 0

11 11 0 0 0 -9 A G G G A G G A 0

syntax is:

iPLEX_to_ped('/path/to/your/csv.csv', '/out/path/to/your/new/ped.txt')

## DOUBLE THE MODE FILTER double_the_mode.py

this script allows you to filter the depth file resulting from VCFTOOLs command --site-mean-depth. The file, for example myvcf.ldepth.mean is a text file that looks like this:

CHROM   POS     MEAN_DEPTH      VAR_DEPTH

NC_037638.1     56596   85.2857 5371.67

NC_037638.1     57208   85.5238 4890.01

NC_037638.1     59559   77.7381 3494.59

NC_037638.1     60391   51.675  2218.99

NC_037638.1     60423   51.625  2207.73


the script finds the mode of the mean site depth, calculates the double of it and any positions over that number will be written into a text document. That resulting text document can be used to remove that sites in VCFTOOLS using --exclude-positions command. 

