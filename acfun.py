#__author__ = 'roots'
#coding=utf-8
#totle=3988457

import time, requests, random, sys, lxml, json
from bs4 import BeautifulSoup
from pymongo import MongoClient

reload(sys)
sys.setdefaultencoding('utf-8')

host = '127.0.0.1'
port = 27017
Mongo_db = MongoClient(host, port)
Mongo_coon = Mongo_db['data']['db']
article_list_info = []
av_list_info = []

headers = [
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
]

######################################################################
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
        # av_list = [plain_text[5], plain_text[1], plain_text[4], plain_text[6]]
        av_dict = {"favorites":plain_text[5],"comment":plain_text[1],"barrage":plain_text[4],"banana":plain_text[6]}
        # print '收藏' + str(plain_text[5])
        # #print '观看人数：' + str(plain_text[0])
        # print '评论' + str(plain_text[1])
        # print '弹幕' + str(plain_text[4])
        # print '香蕉' + str(plain_text[6])

        # favorites += favorites
        # comment += comment
        # barrage += barrage
        # banana += banana
        ####
        #获取av号
        ####
        return av_dict

def article_spider(uid,PageNo):

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

        i = 0
        while (i < len(plain_text['contents'])):
            # print 'www.acfun' + str(plain_text['contents'][i]['url'])
            # print '番号' + str(plain_text['contents'][i]['aid']) #在avspider中获取
            # print '观看人数' + str(plain_text['contents'][i]['views'])
            article_list_info.append(plain_text['contents'][i])
            ll = av_spider(plain_text['contents'][i]['aid'],plain_text['contents'][i]['cid'])
            av_list_info.append(ll)
            i += 1

        if (plain_text['page']['pageNo'] < plain_text['page']['totalPage'] - 1):
            PageNo += 1
            #print PageNo
            article_spider(uid,PageNo)

    return article_list_info, av_list_info
######################################################################


def acfun_spider(user_tag):
    global user_id, headers, file_content


    #user_id += user_divide

    url = "http://acfun.tudou.com/u/%s.aspx#area=post-history" % user_tag
    try:
        source_code = requests.get(url, headers=random.choice(headers))
    except requests.HTTPError:
        source_code = None
    if source_code:
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"lxml")

        # user_divide = '\n' + '--' * 90 + '\n' + '--' * 90 + '\n'
        # file_content += user_divide + '\t' * 4 + 'uid='+ str(user_tag) + ':' + user_divide
        #
        #
        list_soup_id = soup.find('div',{'id':'block-title-banner'}) #用户名
        user_id = list_soup_id.find('p').string.strip() #用户名

        try:
            list_soup_desc = soup.find('p', {'class':'desc'}).string.strip() #他的签名
        except AttributeError:
            list_soup_desc = '无'   #签名

        list_soup_pts = soup.find_all('span', {'class':'pts'})  #投稿数、收听数、听众数
        list_soup_pts_Post = list_soup_pts[0].string.strip() #投稿数
        list_soup_pts_Following =  list_soup_pts[1].string.strip() #他收听的
        list_soup_pts3_Follower =  list_soup_pts[2].string.strip() #听众

        list_soup_userinfo = soup.find('ul', {'id':'list-info-user'})   #用户详细信息
        list_soup_userinfo_detail = list_soup_userinfo.find_all('li')
        list_soup_userinfo_detail_RealName = list_soup_userinfo_detail[0].string.strip() #真实姓名
        list_soup_userinfo_detail_Gender =  list_soup_userinfo_detail[1].string.strip() #性别
        list_soup_userinfo_detail_SexualOrientation = list_soup_userinfo_detail[2].string.strip() #性取向
        list_soup_userinfo_detail_Loaction = list_soup_userinfo_detail[3].string.strip() #所在地
        list_soup_userinfo_detail_RegistrationTime = list_soup_userinfo_detail[4].string.strip() #注册时间
        list_soup_userinfo_detail_Homepage = list_soup_userinfo_detail[5].string.strip() #个人主页
        list_soup_userinfo_detail_QQ = list_soup_userinfo_detail[6].string.strip() #qq
        #
        # file_content += str(user_id) +'\t'+ str(list_soup_desc) +'\t'+ str(list_soup_pts_Post) +'\t'+ str(list_soup_pts_Following) +'\t'+ \
        #                 str(list_soup_pts3_Follower) +'\t'+ str(list_soup_userinfo_detai_RealName) +'\t'+ str(list_soup_userinfo_detai_Gender) +'\t'+ \
        #                 str(list_soup_userinfo_detai_SexualOrientation) +'\t'+ str(list_soup_userinfo_detai_Loaction) +'\t'+ \
        #                 str(list_soup_userinfo_detai_RegistrationTime) +'\t'+ str(list_soup_userinfo_detai_Homepage) +'\t'+ str(list_soup_userinfo_detai_QQ)

        ##################
        PageNo = 1
        (article_list, av_list)=article_spider(user_tag,PageNo)
        listf = []
        for i in range(len(article_list) - 1):
            dd = {"descriptions":list_soup_desc,
                "aid":article_list[i]['aid'],"author":article_list[i]['author'],"uid": article_list[i]['userId'],
                  "url":'www.acfun'+str(article_list[i]['url']),"views":article_list[i]['views'],"cid":article_list[i]['channelId'],
                  "favorites":av_list[i]['favorites'],"barrage":av_list[i]['barrage'],"banana":av_list[i]['banana']}
            # av_dict = {"favorites":plain_text[5],"comment":plain_text[1],"barrage":plain_text[4],"banana":plain_text[6]}
            listf.append(dd)
        #print dd
        ddd = {"content":listf}
        #savedb(user_tag, article_list, av_list)
        #savedb(user_tag, listf)
        savedb(user_tag,ddd)
        ##################



#数据库
# def savedb(uid, article, av):
#     Mongo_coon.insert({
#         "_id":uid,
#         "content":{
#             "article":{"info":article, "av":av},
#
#         }
#     })

def savedb(uid,data):
    Mongo_coon.insert({
        "_id":uid,
        "data":data
    })
#数据库


def do_spider(uid):
    while (uid <= 3888888):
        acfun_spider(uid)
        uid += 1

if __name__ == "__main__":
    uid = 1
    do_spider(uid)