#__author__ = 'roots'
#coding=utf-8

import sys, requests, json, lxml, types
from bs4 import BeautifulSoup

listinfo = []
# listf = []
# listc = []
# listbar = []
# listban = []

def av_spider(aid,cid):

    url = 'http://www.acfun.tv/content_view.aspx?contentId=%s&channelId=%s' % (aid, cid)
    try:
        data = requests.get(url)
    except requests.HTTPError:
        data = None
    if data:
        plain_text = json.loads(data.text)

        favorites = plain_text[5]
        comment = plain_text[1]
        barrage = plain_text[4]
        banana = plain_text[6]

        # print '收藏' + str(plain_text[5])
        # #print '观看人数：' + str(plain_text[0])
        # print '评论' + str(plain_text[1])
        # print '弹幕' + str(plain_text[4])
        # print '香蕉' + str(plain_text[6])

        return (favorites, comment, barrage, banana)


def user_spider(uid,PageNo):
    global comment, barrage, banana

    url = 'http://www.acfun.tv/u/contributeList.aspx?userId=%s&pageSize=10&pageNo=%s&channelId=0' % (uid, PageNo)
    try:
        data = requests.get(url)
    except requests.HTTPError:
        data = None
    if data:
        plain_text = json.loads(data.text)

        # print plain_text.keys()
        # print plain_text['contents']
        # print plain_text['page']['pageNo']
        # print plain_text['page']['totalPage']
        fav = 0
        com = 0
        bar = 0
        ban = 0

        i = 0
        while (i < len(plain_text['contents'])):
            # print 'www.acfun' + str(plain_text['contents'][i]['url'])
            # print '番号' + str(plain_text['contents'][i]['aid'])
            # print '观看人数' + str(plain_text['contents'][i]['views'])
            listinfo.append(plain_text['contents'][i]['url'])
            listinfo.append(plain_text['contents'][i]['aid'])
            listinfo.append(plain_text['contents'][i]['views'])

            (favorites, comment, barrage, banana) = av_spider(plain_text['contents'][i]['aid'],plain_text['contents'][i]['cid'])
            fav += favorites
            com += comment
            bar += barrage
            ban += banana

            # listf.append(fav)
            # listc.append(com)
            # listbar.append(bar)
            # listban.append(ban)

            #print listf

            # comment += comment
            # barrage += barrage
            # banana += banana
            i += 1
            #print favorites
            #print 'i:%d' % i
        # ff += f
        # print 'ff:%d' % ff

        #print 'a:%d' % favorites
        if (plain_text['page']['pageNo'] < plain_text['page']['totalPage']):
            PageNo += 1
            #print PageNo
            user_spider(uid,PageNo)
        # elif(plain_text['page']['pageNo'] == plain_text['page']['totalPage']):

    return listinfo

listinfoo = user_spider(1,1)


###plain_text['page']['pageNo'] < plain_text['page']['totalPage'] - 1 这句话导致少了最后一页的数据。
###
###