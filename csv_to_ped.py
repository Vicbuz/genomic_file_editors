# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:44:09 2021

@author: Victoria Gayle Buswell
"""


import csv
import pandas as pd
import numpy as np
def iPLEX_to_ped(in_file, new_ped):
    ped = open(new_ped,"w")
    with open(in_file) as file:
        iPLEX = pd.read_csv(in_file)
        iPLEX = iPLEX.fillna('0 0') #replace the empty genotypes with the number 0 for ped
        # take all monomorphic sites and add the other base, as all markers nust be biallelic
        iPLEX_G = iPLEX.replace('G', 'G G').replace('GA','G A').replace('GC','G C').replace('GT','G T')
        iPLEX_A = iPLEX_G.replace('A','A A').replace('AG', 'A G').replace('AT','A T').replace('AC','A C')
        iPLEX_T = iPLEX_A.replace('T', 'T T').replace('TA','T A').replace('TG','T G').replace('TC','T C')
        iPLEX_C= iPLEX_T.replace('C','C C').replace('CA','C A').replace('CG','C G').replace('CT','C T')
        iPLEX_final = iPLEX_C
        print(iPLEX_final) # iPLEX FINAL has all the biallelc changes
        melted = iPLEX_final.melt()
        print(melted)
        pivot = iPLEX_final.pivot(index="Sample_Id", columns="Assay_Id")# create a wide not long dataframe
        print(pivot)
        pivot.to_csv(new_ped, index=True)
        
       
    ped.close()

iPLEX_to_ped('/path/to/your/csv.csv', '/out/path/to/your/new/ped.txt')

