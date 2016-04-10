#__author__ = 'roots'

from bs4 import BeautifulSoup
import requests, lxml

header = [{'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'}]
url = "http://acfun.tudou.com/u/2.aspx#area=post-history"
data = requests.get(url)
data_text = data.text
soup = BeautifulSoup(data_text,"lxml")
list_soup = soup.find('div',{'id':'block-title-banner'})
user_id = list_soup.find('p')

list_soup_pts = soup.find_all('span', {'class':'pts'})
list_soup_pts_Post = list_soup_pts[0].string.strip()
try:
    list_soup_desc = soup.find('p', {'class':'desc'}).string.strip()
except AttributeError:
    list_soup_desc = 'no'


list_soup_userinfo = soup.find('ul', {'id':'list-info-user'})
list_soup_userinfo_detai = list_soup_userinfo.find_all('li')
list_soup_userinfo_detai_RealName = list_soup_userinfo_detai[0].string.strip()
#list_soup = soup.find_all('a',{'target': '_blank', 'class': 'name'})
print list_soup_desc

# soup = BeautifulSoup(open("1132885.aspx"))
# print soup