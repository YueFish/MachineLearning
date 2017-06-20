#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import os

#读取中文文件并改变编码
def readfile(srcfilename,desfilename):
    f = open(srcfilename, 'r')
    w = open(desfilename, 'w')
    line = f.readline()
    while line:
        newline = line.decode('GB18030').encode('utf-8')
        print newline,
        print >> w, newline,
        line = f.readline()
    f.close()
    w.close()
