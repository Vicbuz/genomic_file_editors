# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:07:23 2020

@author: vic
"""
# find the mode of the mean site depth. if the depth at a site is double the mode. remove site

import sys
from scipy.stats import mode

def double_the_mode(file_in, file_out):
    depth_file = open(file_in, "r")
    needs_removing = open(file_out, 'w')
    row = depth_file.readlines()[1:]
    a_list =[]
    b_list =[]
    #c_list = []
    for line in row:
        item = line.split()
        a_list.append(item[2])
        a_list.sort()
    #print(a_list)
    for x in a_list:
        b_list.append(float(x))
    #print(b_list)
    one_mode = mode(b_list)
    print(f'The mode is {one_mode[0]}')
    two_modes = one_mode[0]*2
    print(f'Double the mode is {two_modes}') 
# now we know double the mode. so if the item[2] is => double the mode
#we need to write the chromosome and position into a new file

    for line in row:
        item = line.split()    
        if float(item[2]) > two_modes:
            needs_removing.write(f'{item[0]}\t{item[1]}\n')

#double_the_mode('C:/Users/user/Desktop/SNPS/ldepth_site_mean.txt','C:/Users/user/Desktop/SNPS/results_mode')

file_in=str(sys.argv[1])
file_out=str(sys.argv[2])
double_the_mode(file_in, file_out)