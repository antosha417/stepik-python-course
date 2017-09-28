# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 16:01:21 2016

@author: antosha
"""

cr = 0
s, t = (input() for i in range(2))
for i in range(len(s)):
    if s.startswith(t, i):
        cr += 1
print(cr)
