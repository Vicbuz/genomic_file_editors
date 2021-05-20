# -*- coding: utf-8 -*-
"""
Created on Thu May 20 12:44:47 2021

@author: Vic Buswell
This script renames raw fasta files after the directory they are in which is also the sample name,
 with the suffix .1.fq.gz or .2.fq.gz . This was because the samples came with a name that was not easy to identify 
 and had no sample number on but the directory did.
 for example in file 6, contained my sample 6's sequences in forward (_1.fq.gz) and reverse (_2.fq.gz). 
 But the files were called things like E100011477_L1_B5RDAPIctfRAADAA-615_2.fq.gz
 this script changes that to 6.2.fq.gz'
"""
import os
import sys

def rename(path):
        direct = os.listdir(path)
        suffix = ''
        for file in direct:
            suffix = str(file)
            new_dir = path +'/'+ suffix
            #print(new_dir)
            for sample in os.listdir(new_dir):
                #print(sample)
                str_sample = str(sample)
                if '_1.fq' in str_sample:
                    os.rename(new_dir+'/'+sample, new_dir+'/'+suffix+'.1.fq.gz')
                elif '_2.fq' in str_sample:
                    os.rename(new_dir+'/'+sample, new_dir+'/'+suffix+'.2.fq.gz')


#rename(r"C:/path/to/your/directory/of/sample/directories")
path = str(sys.argv[1])
rename(path)
