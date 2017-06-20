#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os
import csv
import random

dirName = os.path.dirname(__file__)
'''
清洗数据类
'''
def washDataDeleteIndex(srcFilename, desFilename):
    srcFile = open(dirName+"/data/"+srcFilename,'r')
    desFilename = open(dirName+"/data/"+desFilename, 'w')
    desFileInfo = csv.writer(desFilename)

    for line in srcFile:
        linelist = line.split(",")
        if linelist.__len__() == 13:
            linelist[-1] = int(linelist[-1].strip())
            desFileInfo.writerow(linelist)
    srcFile.close()
    desFilename.close()

def washDataDelteRepeat(srcFilename,desFilename):
    srcFile = open(dirName + "/data/" + srcFilename, 'r')
    desFilename = open(dirName + "/data/" + desFilename, 'w')
    desFileInfo = csv.writer(desFilename)
    bufferReadLine = ""
    for line in srcFile:
        if line != bufferReadLine:
            linelist = line.split(",")
            linelist[-1] = int(linelist[-1].strip())
            desFileInfo.writerow(linelist)
            bufferReadLine = line
    srcFile.close()
    desFilename.close()

def tailFile(filename):
    with open(dirName + "/data/" + filename) as f:
        num = 0
        for line in f:
            linelist = line.split(",")
            if int(linelist[-1]) ==1:
                print line
            # num += 1
            # if num == 500:
                # break

def countLineNum(filename):
    num = 0
    with open(dirName + "/data/" + filename) as f:
        for line in f:
            num += 1

    return num

def cutData(srcFilaname, desFilename):
    srcFile = open(dirName + "/data/" + srcFilaname, 'r')
    desFilename = open(dirName + "/data/" + desFilename, 'w')
    desFileInfo = csv.writer(desFilename)
    flag = 0
    for line in srcFile:
        linelist = line.split(",")
        linelist[-1] = int(linelist[-1].strip())
        if flag %10 ==0:
            desFileInfo.writerow(linelist)
        flag+=1
    srcFile.close()
    desFilename.close()

def countcatgory(srcFilaname):
    srcFile = open(dirName + "/data/" + srcFilaname, 'r')
    desFileInfo = csv.reader(srcFile)
    list = []
    for line in desFileInfo:
        if line[10] not in list:
            list.append(line[10])
    for i in list:
        print i

if __name__ =='__main__':
    # washDataDeleteIndex("falseLabel_item_yu.csv", "falsesLabel_item_wash.csv")
    # # tailFile("falseLabel_item_delestRepeat.csv")
    # washDataDelteRepeat("falsesLabel_item_wash.csv", "falseLabel_item_washAndDelRe.csv")
    # cutData("allItemInfo.csv", "all_item_info.csv")
    # num =  countLineNum("falseLabel_item_CutWashDelRe.csv")
    # print num
    countcatgory('all_item_info.csv')