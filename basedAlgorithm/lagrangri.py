#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os

from scipy.interpolate import lagrange

DIR = os.path.dirname(__file__)
print DIR

inputfile = DIR+'\data\missing_data.xls'
outputfile =  DIR+'\data\missing_data_procesed.xls'


data = pd.read_excel(inputfile, header= None)

def ployinterp_colum(s, n , k =5):
    y = s[list(range(n-k, n) + list(range(n+1,n+1+k)))] #取前后5个数
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)

for i  in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[i][j] = ployinterp_colum(data[i], j)

data.to_excel(outputfile, header = None, index = False)
