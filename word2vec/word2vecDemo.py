#!/usr/bin/env python
#-*- coding: utf-8 -*-
import jieba
import os
import gensim.models.word2vec as w2c
import logging
from createWordText import *
from logging.handlers import TimedRotatingFileHandler
logFilePath = 'word2vecDemo.log'

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler(logFilePath,
                                   when = 'd',
                                   interval = 1,
                                   backupCount=7)
formatter = logging.Formatter('[%(asctime)s-%(levelname)s - %(message)s]')
handler.setFormatter(formatter)
logger.addHandler(handler)

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

def main():
    pass

if __name__ == "__main__":
    main()
