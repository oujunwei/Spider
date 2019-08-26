# -*- coding:UTF-8 -*-
import random
import time
import requests
from bs4 import BeautifulSoup
import re
import sys
import os
import configparser
from langconv import *
import codecs

path = os.getcwd()
conf = configparser.ConfigParser()
conf.read('setting.conf',encoding='UTF-8')
#文件路径
url_output_file = os.path.join(path,os.path.normpath(conf.get("filepath", "url_output_file")))
commnet_output_file = os.path.join(path,os.path.normpath(conf.get("filepath", "commnet_output_file")))
title_name = os.path.join(path,os.path.normpath(conf.get("filepath", "title_name")))
all_commnet_output_file = os.path.join(path,os.path.normpath(conf.get("filepath", "all_commnet_output_file")))
url = "https://forum.hkgolden.com/Search24.aspx?st=T&searchstring=%u4FEE%u4F8B"

#get a page url
def getStockList(url_output_file, stockURL):

    lst = []
    nextPage=''
    html = getUrl_multiTry(stockURL, 'utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.get("href")
            if href.startswith('view') :
                lst.append(href)
            if  'Search' in href and  'total_pages' in href:
                nextPage = href
        except:
            continue
   #save all url
    #save(url_output_file, lst)
    #print (html)
    return nextPage,lst

#find hiddle url
def getManyURL(lst):
    strs = []
    front_scrit=100
    for i in lst:
        s = i.split('page=')
        if len(s)==2:
            current_scrit = int(s[1])
            if (front_scrit+1)<current_scrit:
                for j in range(front_scrit+1 , current_scrit):
                    strs.append(s[0]+'page='+str(j))
            front_scrit =int(s[1])
    lst.extend(strs)
def getAllPage():
    nextPage_url, lst = getStockList(url_output_file, url)

    save_all_nextPage_url = []
    save_all_nextPage_url.append(url)
    while len(nextPage_url): #read next page url
        nextPage_url = "https://forum.hkgolden.com/" + nextPage_url # produce a new next page url

        if nextPage_url in save_all_nextPage_url:
            break
        save_all_nextPage_url.append(nextPage_url)
        print(nextPage_url)

        nextPage_url ,next_url = getStockList(url_output_file, nextPage_url)
        lst.extend(next_url)

    getManyURL(lst)

    new_urls=[]
    try:
        fr =  open(url_output_file,'r')  #open url file
        conten = fr.readlines()
        lines = len(conten)
    except :
        conten=[]
        lines=0
    for i in lst:
        flg=1
        for j in conten:
            if i == j.strip():
                flg =0
        if flg == 1:
            new_urls.append(i)
    save(url_output_file,new_urls)
    return new_urls, lines

#save all url
def save(url_output_file, re):
    try:
        file = codecs.open(url_output_file, 'a+','utf-8')
        for k in re:
            if len(k) >0:
                file.write(k )
                file.write('\n')
        file.close()
    except Exception as e:
        print(re)
        print (e)


#get all html page using the reqeust method.
def getUrl_multiTry(url, code='utf-8'):
        maxTryNum=10
        for tries in range(maxTryNum):
            try:
                header = {
                        # 'User-Agent': get_user_agent(),
                        'Accept-Language': 'zh-CN,zh;q=0.9'}
                proxies={'http': 'http://127.0.0.1:1080', 'https': 'http://127.0.0.1:1080'}   #set

                r = requests.get(url, headers=header,proxies=proxies )
                r.encoding = code
                break
            except  Exception as e:
                print(str(e))
                time.sleep(3)
                if tries <(maxTryNum-1):
                    continue
                else:
                    print("Has tried %d times to access url %s, all failed!",maxTryNum,url)
                    break

        return r.text

def get_comment(commnet_output_file, url, code='utf-8'):
     html = getUrl_multiTry(url, 'utf-8')
     soup = BeautifulSoup(html, 'html5lib')  #html.parser
     titles = soup.title.string  #get a title of the comment.

     lst = []
     table = soup.find_all('table')

     #save title
     t=[]
     t.append(Converter('zh-hans').convert(titles))
     save(title_name, t)

   #  print (html)
     for i in table:
        try:
            a_comment= ''
            text  = i.find('div',class_='ContentGrid').get_text().replace('\n', '')
            name = i.find('a',href = re.compile('javascript')).get_text().replace('\n', '')
            times = i.find('span',style = re.compile('font-size')).get_text().replace('\n', '')
            a_comment= name+'","' +text +'","' +times;
            lst.append(a_comment)

        except Exception as e:
          #  print (e)
            continue

     commnet_output_file = commnet_output_file  +'.dat'  #produce a new file name.

     #1.In order to address identical data, the method is used.
     new_lst = []
     for i in lst:
             if i not in new_lst:
                 new_lst.append(i)
     #2.use a method to delete incomplete data.
     last_lst = []
     for i in new_lst:
         list = i.split('","')
         if '""' not in list:
             # last_lst.append(i)
             last_lst.append(Converter('zh-hans').convert(i))
     if len(last_lst)==0:
         print(commnet_output_file+'   '+url)
        # print(html)
     save(commnet_output_file, last_lst)

     return last_lst

def get_user_agent():

    user_agents=[
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
    user_agent = random.choice(user_agents)
    return user_agent

if __name__ == '__main__':

    url,lines = getAllPage()
    count=lines+1

    words =[]
    for line in url:
        new_url = 'https://forum.hkgolden.com/' + line # produce a new next page url
        all_lst = get_comment(commnet_output_file + str(count), new_url, code='utf-8')
        count = int(count)+1
        for x in all_lst:
             if len(x.split('","')[1]) > 0:
                words.append(x.split('","')[1])
    save(all_commnet_output_file,words)
