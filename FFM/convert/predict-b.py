#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import hashlib
def hashmac(mac):
    return int(hashlib.md5(mac.encode('utf8')).hexdigest(), 16) % (int(1e+6) - 1) + 1
import os

DIR_NAME = os.path.dirname(__file__)
NR_BINS= int(1e+6)
HEADERS = 'label,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12'


def hashstr(str, nr_bins):
    return int(hashlib.md5(str.encode('utf8')).hexdigest(), 16) % (nr_bins - 1) + 1

def gen_feats(row):
        feats = []
        for j in range(1,13):
            field = 'I{0}'.format(j)
            value = row[field]
            key = field+'-'+str(value)
            feats.append(key)
        return feats

def gen_hashed_fm_feats(feats, nr_bins):
    feats = ['{0}:{1}:1'.format(field-1, hashstr(feat, nr_bins)) for (field, feat) in feats]
    return feats

def makeAprilFFMData(srcFile, desFile):
        dataFile = open(DIR_NAME + "/data/" + srcFile, 'r')
        dataInfo = csv.DictReader(dataFile)
        desFile = open(DIR_NAME + "/data/" + desFile, 'a')

        for row in dataInfo:
            feats=[]
            for feat in gen_feats(row):
                field = feat.split('-')[0]
                field = int(field[1:])
                feats.append((field,feat))
            feats =gen_hashed_fm_feats(feats, NR_BINS)
            desFile.write(row['label'] + ' ' + ' '.join(feats) + '\n' )

        dataFile.close()
        desFile.close()


makeAprilFFMData('all_item_tr.csv','all_item_num_tr.txt')
# print hashmac('00-00-00-00-00-00')
# print hashmac('00-00-00-00-00-01')
# print hashmac('00-00-00-00-00-00')
# print hashmac('00-00-00-00-00-02')
