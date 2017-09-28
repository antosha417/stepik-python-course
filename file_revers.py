# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 19:12:20 2016

@author: antosha
"""

file_name = 'data_set'
with open(file_name, 'r') as f, open('res', 'w') as w:
    lines = f.readlines()
    res = lines[::-1]
    for line in res:    
        w.write(line)
