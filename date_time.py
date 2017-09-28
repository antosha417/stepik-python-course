# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 22:07:45 2016

@author: antosha
"""

import datetime

date = datetime.date(*map(int, input().split()))
res = date + datetime.timedelta(int(input()))
print(' '.join(map(str, [res.year, res.month, res.day])))

