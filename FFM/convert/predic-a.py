#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import csv
import hashlib
import pymongo
import os
DIR_NAME = os.path.dirname(__file__)


class creatIndexData:
    def __init__(self, mongoip, mongoport):
        self._mongoip = mongoip
        self._mongoport = mongoport
        self.connection = pymongo.MongoClient(self._mongoip, self._mongoport)

    def setLogging(self, logFile):
        pass

    def __del__(self):
        self.connection.close()

    def writeTxtFile(self, strline, destfile):
        desFile = open(DIR_NAME + "/data/" + destfile, 'a')
        desFile.write(strline + '\n')
        desFile.close()

    def get_index(self, ):
        pass

    def creatData(self,srcFile,desFile):
        db = self.connection.MediaLibDic
        collectionlist = {"1": "macDic", "2": "nameDic", "3": "languageDic", "6": "directorDic", "7": "castDic",
                          "9": "d_tagDic", "10": "countryDic"}
        dicList = {"1": "mac", "2": "name", "3": "language", "6": "director", "7": "cast",
                   "9": "d_tag", "10": "country"}
        labelElevn = ["免费", '会员免费', '用券', '会员点播']
        labelTelv = ['movie', 'tv']

        dataFile = open(DIR_NAME + "/data/" + srcFile, 'r')
        dataInfo = csv.DictReader(dataFile)

        destinationFile = open(DIR_NAME + "/data/" + desFile, 'a')
        writeInfo = csv.writer(destinationFile)
        i = 0
        for row in dataInfo:
            i +=1
            if i>82065:
                feats= []
                feats.append(row['label'])
                for j in range(1,13):
                    filed = 'A{0}'.format(j)
                    categorylist = row[filed].split('/')
                    if collectionlist.has_key(str(j)):
                        collection= db[collectionlist[str(j)]]
                        value = []
                        for category in categorylist:

                            if category != 'Null':
                                print category
                                index = collection.find_one({dicList[str(j)]: category})
                                index = index['index']
                                value.append(str(index))
                            else:
                                value.append(str(1))

                        valuestr = '/'.join(value)
                        feats.append(valuestr)

                    else:
                        if j == 11:
                            indexla = labelElevn.index(categorylist[0])
                            feats.append(indexla)

                        elif j == 12:
                            indexla = labelTelv.index(categorylist[0])
                            feats.append(indexla)
                        else:
                            feats.append(categorylist[0])
                writeInfo.writerow(feats)
                destinationFile.flush()
        dataFile.close()
        destinationFile.close()


if __name__=="__main__":
    creat = creatIndexData('10.9.201.190', 27017)
    creat.creatData("test.csv", "all_item_tr.csv")
