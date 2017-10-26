# -*- coding:utf-8 -*-
'''
Created on 2016-10-25

@author: kenzhaoyihui
'''

import pymongo
import bson.binary
from pymongo import MongoClient
from cStringIO import StringIO

def insertFile():
    client = MongoClient("mongodb://rhvhlogger:rhvhlogger@127.0.0.1:27017")
    db = client.MongoFile
    coll = db.image

    filename = "/home/yzhao_sherry/Pictures/123456.png".decode('utf-8')
    with open(filename, 'rb') as myimage:
        content = StringIO(myimage.read())
        coll.save(dict(
            content = bson.binary.Binary(content.getvalue()),
            filename = '123456.png'
        ))

def getFile():
    client = MongoClient("mongodb://rhvhlogger:rhvhlogger@127.0.0.1:27017")
    db = client.MongoFile
    coll = db.image

    data  = coll.find_one({'filename': '123456.png'})
    out = open('/home/yzhao_sherry/Pictures/654321.png'.decode('utf-8'), 'wb')
    out.write(data['content'])
    out.close()

if __name__ == '__main__':
    insertFile()
    getFile()