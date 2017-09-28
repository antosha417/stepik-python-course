# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 01:11:58 2016

@author: antosha
"""
import itertools


def primes():
    prime = []
    res = 1
    while True:
        res += 1
        if all(res % i != 0 for i in prime):
            yield res
            prime.append(res)

print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
