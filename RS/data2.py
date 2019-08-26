#-*-coding:utf-8-*-
import numpy as np
import random as rd
import cPickle


data=cPickle.load(open("data.p","rb"))#读取以建好的离散数值型决策表




def get_s1(input1):
    #属性为好的概率（1）好为差
    if input1=="bad":
        s=rd.choice((1,2,3,4,5,6))
        if  s<=2:
            s1=[rd.choice((0.0,0.1,0.2)),rd.choice((0.1,0.2,0.3,0.3)),rd.choice((0.1,0.2,0.3,0.4))]
            s1.sort()
            s1_=[rd.choice((0.5,0.6,0.7)),rd.choice((0.5,0.6,0.7)),rd.choice((0.6,0.7,0.8))]
            s1_.sort()
            s1_1=s1+s1_
            return s1_1
        else:
            s1=[rd.choice((0.0,0.1,0.1)),rd.choice((0.1,0.2,0.2,0.3)),rd.choice((0.1,0.2,0.2,0.3))]
            s1.sort()
            s1_=[rd.choice((0.4,0.5,0.5)),rd.choice((0.5,0.6,0.6)),rd.choice((0.6,0.7,0.7))]
            s1_.sort()
            s1_1=s1+s1_
            return s1_1
    #属性为好的概率（2）好为中
    if input1=="med":
            s1=[rd.choice((0.2,0.3,0.4)),rd.choice((0.3,0.3,0.4,0.5)),rd.choice((0.3,0.4,0.4,0.6))]
            s1.sort()
            s1_=[rd.choice((0.5,0.6,0.6)),rd.choice((0.4,0.5,0.5)),rd.choice((0.3,0.4,0.5))]
            s1_.sort()
            s1_1=s1+s1_
            return s1_1
     #属性为好的概率（2）好为好
    if input1=="good":
        s=rd.choice((1,2,3,4,5,6))
        if  s<=2:
            s1=[rd.choice((0.5,0.6,0.6)),rd.choice((0.6,0.6,0.7,0.7)),rd.choice((0.7,0.7,0.5,0.8))]
            s1.sort()
            s1_=[rd.choice((0.2,0.3,0.4)),rd.choice((0.2,0.3,0.3)),rd.choice((0.3,0.3,0.2))]
            s1_.sort()
            s1_1=s1+s1_
            return s1_1
        else:
            s1=[rd.choice((0.7,0.7,0.8)),rd.choice((0.6,0.8,0.7,0.8)),rd.choice((0.8,0.8,0.9,0.9))]
            s1.sort()
            s1_=[rd.choice((0.0,0.0,0.1)),rd.choice((0.1,0.1,0.2)),rd.choice((0.2,0.1,0.2))]
            s1_.sort()
            s1_1=s1+s1_
            return s1_1


def shuziTOmohu1(a):
    '''
    将一个实数值转化为三角模糊数犹豫直觉模糊集
    :param a:
    :return:
    '''
    san_list=[]
    if a==1:
        s=rd.choice((1,2,3,4,5,6))
        if  s<=2:
            san_list.append(get_s1("good"))
            san_list.append(get_s1("med"))
            san_list.append(get_s1("med"))
            return san_list
        else:
            san_list.append(get_s1("good"))
            san_list.append(get_s1("med"))
            san_list.append(get_s1("bad"))
            return san_list
    elif a==2:
        s=rd.choice((1,2,3,4,5,6))
        if  s<=2:
            san_list.append(get_s1("med"))
            san_list.append(get_s1("good"))
            san_list.append(get_s1("bad"))
            return san_list
        else:
            san_list.append(get_s1("bad"))
            san_list.append(get_s1("good"))
            san_list.append(get_s1("med"))
            return san_list
    elif a==3:
        s=rd.choice((1,2,3,4,5,6))
        if  s<=2:
            san_list.append(get_s1("med"))
            san_list.append(get_s1("med"))
            san_list.append(get_s1("good"))
            return san_list
        else:
            san_list.append(get_s1("bad"))
            san_list.append(get_s1("med"))
            san_list.append(get_s1("good"))
            return san_list



def shuziTOmohu(data):
    '''
    将数值型数据转化为模糊性数据
    :param data:
    :return:
    '''
    data_dict={}#模糊数字典：key为对象标注 value为属性三角模糊值
    for i in range(data.shape[0]):
        sent_list=[]
        for j in range(data.shape[1]-1):
            sent_list.append(shuziTOmohu1(int(data[i][j])))
        sent_list.append(int(data[i][-1]))
        C="C%d"%i
        data_dict[C]=sent_list
    return data_dict

data_dict=shuziTOmohu(data)
cPickle.dump(data_dict,open("data_dict.p","wb"))

for key in data_dict:
    print(key ,data_dict[key])