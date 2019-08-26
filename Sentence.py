import jieba
import os
import configparser
import codecs
import re

path = os.getcwd()
conf = configparser.ConfigParser()
conf.read('setting.conf',encoding='UTF-8')
all_commnet_output_file = os.path.join(path,os.path.normpath(conf.get("filepath", "all_commnet_output_file")))
commnet_output_file = os.path.join(path,os.path.normpath(conf.get("filepath", "commnet_output_file")))
trainfile = os.path.join(path,os.path.normpath(conf.get("filepath", "trainfile")))
chinsesstoptxt = os.path.join(path,os.path.normpath(conf.get("filepath", "chinsesstoptxt")))
# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in codecs.open(chinsesstoptxt ,encoding='UTF-8').readlines()]
    return stopwords

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

# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    jieba.suggest_freq('林郑月娥', True)
    jieba.suggest_freq('林郑', True)
    sentence_depart = jieba.lcut_for_search(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

def unite_files():
    strs = []
    for i in range(1877):
        f = codecs.open(commnet_output_file + ' (' + str(i+1) + ').dat', 'r','utf-8')
        rd = f.readlines()

        for j in rd:
            lit = j.split('","')
            strs.append(lit[1])
    save(all_commnet_output_file,strs)

inputs =codecs.open(all_commnet_output_file,'r','utf-8')  #open url file
# conten = fr.readlines()
outputs = codecs.open(trainfile, 'a+','utf-8')


# seg_list = jieba.cut(conten, cut_all=False)

for line in inputs:
    results=re.compile("https://[a-zA-Z0-9.?/&=:]*",re.S)
    dd=results.sub("",line)
    line_seg = seg_depart(re.compile("http://[a-zA-Z0-9.?/&=:]*",re.S).sub("",dd))
    outputs.write(line_seg + '\n')
    print("-------------------正在分词和去停用词-----------")
outputs.close()
inputs.close()
print("删除停用词和分词成功！！！")

# def line_seg(str):
#     dedup_str = ''
#     for char in str:
#         if not char in dedup_list:
#             dedup_str += char
#
#     return dedup_list
#
# str = input('line_seg')
# print(line_seg(str))
