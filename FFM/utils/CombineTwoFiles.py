#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import os
dirName =  os.path.dirname(__file__)

aFile = open(dirName+"/data/trueLabel_item_washAndDeletRe.csv", 'r')
aInfo = csv.reader(aFile)

# bFile = open(dirName+"/data/trueLabel_item_yu.csv", "r")
# bInfo = csv.reader(bFile)


cTestFile = open(dirName+"/data/allItemInfo.csv","a")
cInfo = csv.writer(cTestFile)

for line in aInfo:
    cInfo.writerow(line)




aFile.close()
# bFile.close()
cTestFile.close()
