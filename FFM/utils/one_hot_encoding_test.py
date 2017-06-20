#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn import preprocessing
from sklearn.linear_model import  LogisticRegression

enc = preprocessing.OneHotEncoder()
array = [[0,0,3],[1,1,0],[0,2,1],[1,0,2]]
enc.fit(array)

array1 = enc.transform([[0,1,1]]).toarray()

print array1