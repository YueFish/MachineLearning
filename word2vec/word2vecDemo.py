#!/usr/bin/env python
#-*- coding: utf-8 -*-
import jieba
import os
import string
import gensim.models.word2vec as w2v
import logging
# from createWordText import *
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


#中文分词
def spilitWord():
    f = open('item_text.txt', 'r')
    w = open('item_cut_text.txt', 'w')
    line = f.readline()

    while line:
        print line
        newline = jieba.cut(line, cut_all=False)
        newline = ' '.join(newline).encode('utf-8')
        str_out = newline.translate(None, string.punctuation)
        str_out = str_out.replace('？','').replace('，','').replace("《",'').replace("》",'')\
        .replace("！", '').replace('?', '').replace("· ",'').replace("·", '').replace(".", '')\
        .replace(" ：", "")
        print str_out
        w.write(str_out+'\n')
        w.flush()
        line = f.readline()
    w.close()
    f.close()

def word2vecModel():
    model_file_name = "item_model.txt"
    #训练模型
    sentences = w2v.LineSentence('item_cut_text.txt')
    model = w2v.Word2Vec(sentences, size = 20, window = 5, min_count=5, workers=4)
    model.save(model_file_name)
    print model.similarity('吉祥'.decode('utf-8'),'天宝'.decode('utf-8'))
    for k in model.similar_by_word('国家机密'.decode('utf-8')):
        print k[0], k[1]

model=w2v.Word2Vec.load('item_model.txt')
y2= model.most_similar('成龙'.decode('utf-8'),topn=20)
for k in y2:
    print k[0], k[1]


