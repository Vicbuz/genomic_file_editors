# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:07:23 2020

@author: vic
"""
# find the mode of the mean site depth. if the depth at a site is double the mode. remove site
from scipy.stats import mode

def double_the_mode(file_in, file_out):
    depth_file = open(file_in, "r")
    needs_removing = open(file_out, 'w')
    row = depth_file.readlines()[1:]
    a_list =[]
    b_list =[]
    c_list = []
    for line in row:
        item = line.split()
        a_list.append(item[2])
        a_list.sort()
    print(a_list)
    for x in a_list:
        b_list.append(float(x))
    for y in b_list:
        c_list.append(round(y))
    one_mode = mode(c_list)
    double_the_mode = one_mode[0]*2
    return double_the_mode

        
        
    
        
        #if int(item[2]) > depth_max:
            #needs_removing.write(f'{item[0]}\t{item[1]}\n')

double_the_mode('C:/path/to/your/ldepth_site_mean.txt','C:/path/to/results')
