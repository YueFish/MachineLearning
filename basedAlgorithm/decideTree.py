#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import  log


def calcShannonEnt(dataset):
    numEntries = len(dataset)
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -=prob*log(prob,2)
    return shannonEnt

def createDataSet():
    dataset = [[1,1,"yes"],
               [1,1,"yes"],
               [1,0,"no"],
               [0,1,"no"],
               [0,1,"no"]]
    labels = ["no surfacing ", "flippers"]
    return dataset, labels

def splitDataset(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0])
    baseEntropy = calcShannonEnt(dataSet)
    baseInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataset(dataSet, i ,value)
            prob = len(subDataSet)
            newEntropy += prob *calcShannonEnt(subDataSet)
        infoGain = baseEntropy- newEntropy
        if (infoGain > baseInfoGain):
            baseInfoGain = infoGain
            bestFeature = i
    return bestFeature

if __name__ == "__main__":
    mydata , labels = createDataSet()
    print chooseBestFeatureToSplit(mydata)