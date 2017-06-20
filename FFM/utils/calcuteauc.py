#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.metrics import roc_auc_score
import os

DIR_NAME = os.path.dirname(__file__)



score = []
label = []
srcfd = open(DIR_NAME+"/data/output.txt", 'r')
labelfd = open(DIR_NAME+"/data/all_item_random_pr.txt", 'r')
scrlines = srcfd.readlines()
labellines = labelfd.readlines()
for i in scrlines:
    score.append(float(i.strip()))
for j in labellines:
    label.append(int(j.split(" ")[0]))
from sklearn import metrics
test_auc = metrics.roc_auc_score(label,score)
print 'AUC=',test_auc
# num = 0
# for k in range(len(score)):
#     flag = 0
#     if score[k] > auc:
#         flag = 1
#     else:
#         flag = 0
#     if flag == label[k]:
#         num += 1
# print num
# print float(num/200.0)


srcfd.close()
labelfd.close()