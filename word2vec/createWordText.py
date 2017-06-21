#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
Field = "name,director,cast,summary,tag,d_tag,country,d_type,refereredNames"

def getAllChineseField():
    '''
       获取媒体库完整电影和TV数据
       构成中文预料文本
    '''
    connection = pymongo.MongoClient('10.9.201.190', 27017)
    db = connection.douban20170227
    collection = db.chiq_video_optimizationtoday
    a = collection.find({"tencent": "1", "model": {"$in": ["movie", "tv"]}})
    return a

def saveWordText(item_list_text):
    '''

    :return:
    '''
    w = open('item_text.txt', 'w')
    item_list_t = item_list_text
    Field_list = Field.split(',')
    for item in item_list_t:
        line = ""
        seq = []
        for field in Field_list:
            if item.has_key(field):
                seq.append(item[field])
        line = ' '.join(seq)
        line = line.replace("/", ' ')
        line = line.encode('utf-8')
        w.write(line+'\n')
        w.flush()
    w.close()


item_list = getAllChineseField()
saveWordText(item_list)

