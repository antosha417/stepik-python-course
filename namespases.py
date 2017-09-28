# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 20:05:16 2016

@author: antosha
"""

class Namespase:
    def __init__(self, name, par_name):
        self.names = []
        self.name = name
        self.parent = par_name
        
    def add(self, name):
        self.names.append(name)

    def contains(self, name):
        return name in self.names
        
spases = {'global': Namespase('global', None)}

n = int(input())
for i in range(n):
    line = input().split()
    if line[0] == 'add':
        spases[line[1]].add(line[2])
    if line[0] == 'create':
        spases[line[1]] = Namespase(line[1], line[2])
    if line[0] == 'get':
        error = True
        name = line[1]        
        while name != None:
            if spases[name].contains(line[2]):
                error = False                
                print(name)
                break
            name = spases[name].parent
        if error:
            print(None)
    
'''
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
'''