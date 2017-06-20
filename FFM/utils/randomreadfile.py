#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8
import random
from sets import Set
import os
dirName = os.path.dirname(__file__)

def copyfile(srcfile, dstfile, linenum):
    """
        get linenum different lines out from srcfile at random
        and write them into dstfile
    """
    result = []
    numrandom = []
    ret = False
    try:
        srcfd = open(srcfile, 'r')
    except IOError:
        print 'srcfile doesnot exist!'
        return ret
    try:
        dstfd = open(dstfile, 'w')
    except IOError:
        print 'dstfile doesnot exist!'
        return ret
    srclines = srcfd.readlines()
    srclen = len(srclines)
    for num in range(srclen):
        numrandom.append(num)
    random.shuffle(numrandom)
    for s in numrandom:
        result.append(srclines[s])
    for content in Set(result):
        dstfd.write(content)
    srcfd.close()
    dstfd.close()
    ret = True
    return ret


if __name__ == "__main__":
    print copyfile(dirName+"/data/all_item_num_tr.txt", dirName+"/data/all_item_random_tr.txt", 103730)