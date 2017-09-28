# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 00:25:55 2016

@author: antosha
"""

from __future__ import print_function

import os
from zipfile import ZipFile


def unzip(file_name):
    '''
    args: (file_name)
    unzip all files from archive
    '''
    zip_file = ZipFile(file_name)
    zip_file.extractall()

unzip('main.zip')


ANSWER = []
for path, direct, files in os.walk('main'):
    if any(file[len(file)-3:] == '.py' for file in files):
        ANSWER.append(path)
ANSWER.sort()
for path in ANSWER:
    print(path)
