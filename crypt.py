# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:42:29 2016

@author: antosha
"""

import simplecrypt


data = simplecrypt.encrypt('123', 'hello')

print(simplecrypt.decrypt('123', data))


with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    
print(encrypted)
print()
    
with open('passwords.txt', 'r') as f:
    passwords = f.readlines()
    
for i in range(len(passwords)):
    passwords[i] = passwords[i].strip()
    # print(passwords[i])

for password in passwords:
    try:    
        print(simplecrypt.decrypt(password, encrypted))
    except ValueError:
        print(password)

