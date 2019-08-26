import jieba
import os
import configparser
import codecs
import re
from langconv import *

path = os.getcwd()
conf = configparser.ConfigParser()
conf.read('setting.conf',encoding='UTF-8')
all_commnet_output_file = os.path.join(path,os.path.normpath(conf.get("filepath", "all_commnet_output_file")))
commnet_output_file = os.path.join(path,os.path.normpath(conf.get("filepath", "commnet_output_file")))
trainfile = os.path.join(path,os.path.normpath(conf.get("filepath", "trainfile")))
chinsesstoptxt = os.path.join(path,os.path.normpath(conf.get("filepath", "chinsesstoptxt")))

# #读取舆论制造者的评论信息
path = "D:/Spider/data/inform" #待读取文件的文件夹绝对地址
files = os.listdir(path) #获得文件夹中所有文件的名称列表
list = []
for file in files:
  f = open(path+"/"+file,'rb')

  f.seek(0,0)
  print(file)
  a=f.readlines()
  s = [] #初始化列表
  for ii in a: #遍历文件，一行行读取，并添加到s中
    s.append(ii.decode('utf-8'))
  list.append(s) #将s添加到list中



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

words=[]
# fr = open(commnet_output_file,'r')
# content = fr.readlines()
str=''
cout =0
for x in list:
    cout =cout+1
    if len(x)>0:
         print(x[0])

         if cout>3000:
             print(cout)
         if x[0].split('","')[0].strip('"') =='基魔大和' and len(x[0].split('","')[1]) > 0:
             for y in x:
                words.append(y.split('","')[1])
save(all_commnet_output_file, words)