#__author__ = 'roots'
#coding=utf-8

import datetime
from pymongo import MongoClient

host = '127.0.0.1'
port = 27017
Mongo_db = MongoClient(host, port)
Mongo_coon = Mongo_db['data']['db']

d = {u'channelId': 110, u'userId': 1, u'sign': u'\u738B\u654F\u5218\u9759\u5BA2\u670D2\u5BA2\u670D1', u'releaseDate': 1329323384000L, u'titleImg': u'http://cdn.aixifan.com/dotnet/20120923/style/image/cover.png', u'isArticle': 1, u'title': u'\u5173\u4e8e\u5185\u6838\u5207\u6362\u5ef6\u8fdf\u5207\u6362\u7684\u901a\u77e5', u'userImg': u'http://cdn.aixifan.com/dotnet/artemis/u/cms/www/201303/26132122j2lg.jpg', u'comments': 144, u'score': 22348, u'username': u'admin', u'description': u'\u65f6\u5728\u7cfb\u7edf\u4e2d\u79fb\u9664\uff0c\u7531\u4e8e\u6570\u636e\u5e93\u8bbe\u8ba1\u7684\u4e00\u4e9b\u590d\u6742\u6027\u4ee5\u53caMSSQL\u7684\u4e00\u4e9b\u7279\u6027\uff0c\u6211\u4eec\u9700\u8981\u4e00\u5b9a\u7684\u65f6\u95f4\u3002\u6b64\u5916\uff0c\u4e3a\u914d\u5408\u516c\u5b89\u90e8\u95e8\u4e25\u6253\u5de5\u4f5c\u8fdb\u884c\uff0c\u6211\u4eec\u9700\u8981\u5728\u672c\u5468\u5185\u79ef\u6781\u5f00\u5c55\u9488\u5bf9\u7ad9\u5185\u8272\u60c5\u3001\u8fdd\u6cd5\u4fe1\u606f\u7684\u8bb0\u5f55\u548c\u4e0a\u62a5\u5de5\u4f5c\uff0c\u5de5\u4f5c\u91cf\u5f88\u5927\uff0c\u6545\u7cfb\u7edf\u5347\u7ea7\u65f6\u95f4\u9884\u8ba1\u987a\u5ef6\u5230\u4e0b\u5468\u4e00\u3002\u7ed9\u60a8\u5e26\u6765\u7684\u4e0d\u4fbf\u6211\u4eec\u6df1\u8868\u6b49\u610f\u3002&nbsp;A', u'views': 12201, u'aid': 300567, u'stows': 9, u'success': True, u'cid': 300567, u'url': u'/a/ac300567', u'author': u'admin', u'errorlog': u'', u'avatar': u'http://cdn.aixifan.com/dotnet/artemis/u/cms/www/201303/26132122j2lg.jpg', u'allowDanmaku': 1, u'time': 0, u'contentClass': u''}
a = [u'\u738B\u654F'
     u'\u5218\u9759'
     u'\u5BA2\u670D2'
     u'\u5BA2\u670D1'
     u'\u6D1B\u9633'
     u'\u9B4F\u8273\u854A'
     u'\u6F58\u4EAD'
     u'\u8096\u73B2'
     u'\u5BA2\u670D01'
     u'\u5468\u6167'
     u'\u738B\u83F2'
     u'\u5468\u6167'
     u'\u4EDD\u5C0F\u82B3'
    u'\u8D75\u8DEF\u7476'
    u'\u83F2\u83F2'
    u'\u90D1\u4F20\u4E3D'
]
print a
# def save(data):  # data 表示需要存储的单条记录（如上面的json，在Python中表现形式为dict）
#     #data['_id'] = int(data['aid'])  # 理由已经解释
#     #data['updateTime'] = datetime.datetime.now()  # 我们最好记录下更新的时间
#
#         Mongo_coon.insert({
#         "_id": data['aid'],#番号
#         "cid": data['channelId'],#
#         "uid": data['userId'],#用户id
#         "author": data['author'],#用户名
#         "title": data['title'],#文章名
#         "url": 'acfun'+ data['url']#url
#         # title
#         }
#         # filter={'_id': data['aid']},
#         # update={'$set': data},
#         # upsert=True
#     )
# save(d)
