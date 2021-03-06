#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import *
import operator

def creatDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

group, labels = creatDataSet()

def classify0(inX, dataSet, label, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1))- dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = label[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) +1
    sortedClassCount = sorted(classCount.iteritems(),
                              key = operator.itemgetter(1),
                              reverse=True)
    return sortedClassCount[0][0]

print classify0([1.0,1.0], group,labels, 3)