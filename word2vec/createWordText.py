#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo


def getAllChineseField():
    '''
       获取媒体库完整电影和TV数据
       构成中文预料文本
    '''

    db = self.connection.douban20170227
    collection = db.chiq_video_optimizationtoday
    a = collection.find({"tencent": "1", "model": {"$in": ["movie", "tv"]}})
    return a