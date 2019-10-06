import WriteFile
import os
import configparser
import datetime
import re

path = os.getcwd()
conf = configparser.ConfigParser()
conf.read('setting.conf',encoding='UTF-8')
url_output_file = os.path.join(path,os.path.normpath(conf.get("filepath", "url_output_file")))
all_commnet_output_file = os.path.join(path,os.path.normpath(conf.get("filepath", "all_commnet_output_file")))
title_name = os.path.join(path,os.path.normpath(conf.get("filepath", "title_name")))
commnet_output_file = os.path.join(path,os.path.normpath(conf.get("filepath", "commnet_output_file")))
statics = os.path.join(path,os.path.normpath(conf.get("filepath", "statistic")))
# #读取舆论制造者的评论信息
# path = "C:/Users/xdw-001/Documents/GitHub/Spider/data/inform" #待读取文件的文件夹绝对地址
# files = os.listdir(path) #获得文件夹中所有文件的名称列表
# list = []

def getTitleInfor():
    url = WriteFile.readFile(url_output_file,'r','UTF-8') # get all url
    All_title = WriteFile.readFile(title_name,'r','UTF-8') # read all titles.
    count=0;
    for index in range(len(url)):
        if(len(url[index].split('&page=')))==1: # if it can be splited by &page=, it must be an url of the title.
            count += 1
            a = WriteFile.readFile(commnet_output_file+str(index+1)+'.dat','r','UTF-8')
            # save title+name+comment+time
            WriteFile.save(statics+'\\'+'tnct.dat',All_title[index].replace("\n","")+'","'+a[0].replace("\n",""))
    print('总计发帖量：'+str(count)+'条')


def getAllComment_tittle():
    url = WriteFile.readFile(url_output_file,'r','UTF-8') # get all url
    All_title =WriteFile.readFile(title_name,'r','UTF-8') # read all titles.
    title =[]
    line = []
    items_idx = 0
    for u in url:
        items_idx += 1
        if(len(u.split('&page=')))==1: # if it can be splited by &page=, it must be an url of the title.
            title.append(u)
            line.append(items_idx)





    print(statics)
    for x in range(len(title)):

        a = WriteFile.readFile(commnet_output_file+str(line[x])+'.dat','r','UTF-8')
        print(All_title[line[x]])
        # print(a[0])
        # save title+name+comment+time
        WriteFile.save(statics+'\\'+'tnct.dat',All_title[line[x]-1].replace("\n","")+'","'+a[0].replace("\n",""))

        #save all comments, in which a person deliver a title.
        b= statics+'\\'+str(x+1)+'.dat'
        WriteFile.save(b,a)
        for u in range(len(url)):
            if title[x].replace("\n","")  in (url[u]) and len(title[x]) != len(url[u]):
                WriteFile.save(b,WriteFile.readFile(commnet_output_file+str(u+1)+'.dat','r','UTF-8'))
                # print(url[u])

#handle the time.
def distinction(beginDate,middleDate,endDate):
    url = WriteFile.readFile(url_output_file,'r','UTF-8') # get all url
    results=re.compile("(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]",re.S)

    for index in range(len(url)):
        comm = WriteFile.readFile(commnet_output_file+str(index+1)+'.dat','r','UTF-8') # get all url
        if isinstance(comm,list):
            for i in range(len(comm)):
                if(len(comm[i].split('","')) ==3):
                    try:
                        date = datetime.datetime.strptime(comm[i].split('","')[2].strip().replace("\n",""),'%d/%m/%Y %H:%M')

                        if(datetime.datetime.strptime(beginDate,'%Y/%m/%d')<=date and date < datetime.datetime.strptime(middleDate,'%Y/%m/%d')):
                            WriteFile.save(statics+'\\'+'begin.dat',results.sub("",comm[i].split('","')[1]))
                        elif(datetime.datetime.strptime(middleDate,'%Y/%m/%d')<=date and date <= datetime.datetime.strptime(endDate,'%Y/%m/%d')):
                            WriteFile.save(statics+'\\'+'meddile.dat',results.sub("",comm[i].split('","')[1]))
                        elif(datetime.datetime.strptime(endDate,'%Y/%m/%d')< date):
                            WriteFile.save(statics+'\\'+'end.dat',results.sub("",comm[i].split('","')[1]))
                    except Exception as e:
                        print(comm[i])
                        print(e)
        else :
            a = WriteFile.readFile(commnet_output_file+str(index+1)+'.dat','r','UTF-8')
            # save title+name+comment+time
    print('总计发帖量：'+'条')

# for file in files:
#   a = WriteFile.readFile(path+"/"+file,'rb')
#   s = [] #初始化列表
#   for ii in a: #遍历文件，一行行读取，并添加到s中
#     s.append(ii.decode('utf-8'))
#   list.append(s) #将s添加到list中
#
#
# words=[]
# # fr = open(commnet_output_file,'r')
# # content = fr.readlines()
# str=''
# cout =0
# for x in list:
#     cout =cout+1
#     if len(x)>0:
#          print(x[0])
#
#          if cout>3000:
#              print(cout)
#          if x[0].split('","')[0].strip('"') =='基魔大和' and len(x[0].split('","')[1]) > 0:
#              for y in x:
#                 words.append(y.split('","')[1])
# WriteFile.save(all_commnet_output_file, words)

if __name__ == '__main__':
    distinction('2019/4/25','2019/6/1','2019/7/9')
    # getTitleInfor()
    # getAllComment_tittle()