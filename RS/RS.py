#-*-coding:utf-8-*-
import numpy as np
import pickle as p

data_dict=p.load(open("data_dict.p",'rb'))
data_list=[]
for index in range(len(data_dict)):
    C="C%d"%index
    data_list.append(data_dict[C])




def defen(s):
    '''
    计算每个模糊数中每个维度的得分函数
    :param s:
    :return:
    '''
    ss=0.0
    for line in s:
        s1=(line[0]+2*line[1]+line[2])/4.0
        s2=(line[3]+2*line[4]+line[5])/4.0
        ss+=(s1-s2)
    return ss
def defen1(line):
    '''
    计算每个模糊数中每个维度的得分函数
    :param s:
    :return:
    '''
    ss=0.0
    s1=(line[0]+2*line[1]+line[2])/4.0
    s2=(line[3]+2*line[4]+line[5])/4.0
    ss+=(s1-s2)
    return ss
def find_lixiangdian_pos(colum_list_ele):
    '''
    每个属性下的理想点
    :param colum_list_ele:
    :return:
    '''
    sum_list=[]
    for line in colum_list_ele:
        sum_list.append(defen(line))

    spos=[i for i in range(len(sum_list)) if sum_list[i]==max(sum_list)]

    return colum_list_ele[spos[0]]
def find_lixiangdian_pos1(colum_list_ele):
    '''
    每个属性下的理想点
    :param colum_list_ele:
    :return:
    '''
    sum_list=[]
    s1_list=[]
    s2_list=[]
    s3_list=[]
    for line in colum_list_ele:
        #sum_list.append(defen(line))
        s1_list.append(defen1(line[0]))
        s2_list.append(defen1(line[1]))
        s3_list.append(defen1(line[2]))
    spos1=[i for i in range(len(s1_list)) if s1_list[i]==max(s1_list)]
    spos2=[i for i in range(len(s2_list)) if s2_list[i]==max(s2_list)]
    spos3=[i for i in range(len(s3_list)) if s3_list[i]==max(s3_list)]
    #spos=[i for i in range(len(sum_list)) if sum_list[i]==max(sum_list)]
    s1=colum_list_ele[spos1[0]][0]
    s2=colum_list_ele[spos2[0]][1]
    s3=colum_list_ele[spos3[0]][2]
    ss=[]
    ss.append(s1)
    ss.append(s2)
    ss.append(s3)

    return ss

def find_lixiangdian_neg(colum_list_ele):
    '''
    每个属性下的理想点
    :param colum_list_ele:
    :return:
    '''
    sum_list=[]
    for line in colum_list_ele:
        sum_list.append(defen(line))

    sneg=[i for i in range(len(sum_list)) if sum_list[i]==min(sum_list)]

    return colum_list_ele[sneg[0]]

def find_lixiangdian_neg1(colum_list_ele):
    '''
    每个属性下的理想点
    :param colum_list_ele:
    :return:
    '''
    sum_list=[]
    s1_list=[]
    s2_list=[]
    s3_list=[]
    for line in colum_list_ele:
        #sum_list.append(defen(line))
        s1_list.append(defen1(line[0]))
        s2_list.append(defen1(line[1]))
        s3_list.append(defen1(line[2]))
    spos1=[i for i in range(len(s1_list)) if s1_list[i]==min(s1_list)]
    spos2=[i for i in range(len(s2_list)) if s2_list[i]==min(s2_list)]
    spos3=[i for i in range(len(s3_list)) if s3_list[i]==min(s3_list)]
    #spos=[i for i in range(len(sum_list)) if sum_list[i]==max(sum_list)]
    s1=colum_list_ele[spos1[0]][0]
    s2=colum_list_ele[spos2[0]][1]
    s3=colum_list_ele[spos3[0]][2]
    ss=[]
    ss.append(s1)
    ss.append(s2)
    ss.append(s3)

    return ss


def find_lixiangdian(data_list):
    '''
    寻找data_dict中每个属性的正负理想点
    :param data_dict:
    :return:
    '''
    colum_list=[]#每个属性的所有值 21个
    for j in range(len(data_list[0])-1):
        ss=[]
        for i in range(len(data_list)):
            ss.append(data_list[i][j])
        colum_list.append(ss)
    data_pos=[]
    data_neg=[]
    for line in colum_list:
        data_pos.append(find_lixiangdian_pos(line))
        data_neg.append(find_lixiangdian_neg(line))
    return data_pos,data_neg

data_pos,data_neg=find_lixiangdian(data_list)
ii=1
for i,j in zip(data_pos,data_neg):
    print ("第%d个指标的正理想点"%ii ,i)
    print ("第%d个指标的负理想点"%ii ,j)
    ii+=1

def distance1(s1,s2):
    '''
    两个三角模糊数犹豫直觉模糊集的距离
    :param s1:
    :param s2:
    :return:
    '''
    ss1=defen(s1)
    ss2=defen(s2)
    return abs((ss1-ss2))
def distance(data_list,data_pos,data_neg):
    '''
    每个属性值的正负距离和贴近度矩阵
    :param data_list:
    :param data_pos:
    :param data_neg:
    :return:
    '''
    data_array=np.zeros((len(data_list),len(data_list[0])))
    jj=1
    for j in range(len(data_list)):
        print ("\n"+"对象U%d下各属性值的正负理想点距离"%jj)
        jj+=1
        for i in range(len(data_list[j])-1):
            distance_pos=distance1(data_list[j][i],data_pos[i])
            distance_neg=distance1(data_list[j][i],data_neg[i])
            print( "[",distance_pos,distance_neg,"]",)

    ii=1
    for j in range(len(data_list)):
        print ("\n"+"对象U%d下各属性值的贴近度"%ii)
        ii+=1
        for i in range(len(data_list[j])-1):
            distance_pos=distance1(data_list[j][i],data_pos[i])
            distance_neg=distance1(data_list[j][i],data_neg[i])
            ss=distance_neg/(distance_neg+distance_pos)
            print ("%.2f"%ss,)
            if  ss<=0.44:
                ss1=1
            elif ss>0.44 and ss<=0.65:
                ss1=2
            else:
                ss1=3
            data_array[j][i]=int(ss1)
        data_array[j][-1]=int(data_list[j][-1])
    return data_array






data_array=distance(data_list,data_pos,data_neg)#处理完毕的层次集决策表

file1=open("data.txt",'w')
for line in data_array:
    for ele in line:
        ele=int(ele)
        file1.write(str(ele))
        file1.write(" ")
    file1.write("\n")
p.dump(data_array,open("data_array.p",'wb'))
print ("\n")
print (data_array)













































C1=[[0.2, 0.4, 0.6, 0.5, 0.5, 0.6], [0.3, 0.4, 0.5, 0.3, 0.5, 0.5], [0.7, 0.8, 0.9, 0.0, 0.1, 0.2]]
C1_=[[0.1, 0.1, 0.2, 0.5, 0.6, 0.6], [0.6, 0.7, 0.7, 0.3, 0.3, 0.4], [0.3, 0.3, 0.3, 0.3, 0.4, 0.6]]
C2=[[0.8, 0.8, 0.9, 0.0, 0.1, 0.2], [0.4, 0.4, 0.6, 0.3, 0.5, 0.6], [0.3, 0.4, 0.5, 0.5, 0.5, 0.6]]
C2_=[[0.1, 0.1, 0.3, 0.5, 0.5, 0.7], [0.2, 0.3, 0.4, 0.4, 0.4, 0.6], [0.5, 0.6, 0.6, 0.2, 0.3, 0.3]]
C3=[[0.7, 0.8, 0.9, 0.0, 0.1, 0.2], [0.2, 0.3, 0.5, 0.3, 0.5, 0.5], [0.4, 0.5, 0.6, 0.3, 0.5, 0.6]]
C3_=[[0.0, 0.1, 0.3, 0.5, 0.7, 0.7], [0.6, 0.6, 0.8, 0.3, 0.3, 0.3], [0.3, 0.4, 0.6, 0.4, 0.5, 0.6]]
C4=[[0.8, 0.8, 0.9, 0.0, 0.1, 0.2], [0.2, 0.3, 0.6, 0.5, 0.5, 0.5], [0.3, 0.3, 0.4, 0.4, 0.4, 0.6]]
C4_=[[0.0, 0.1, 0.2, 0.7, 0.7, 0.8], [0.6, 0.6, 0.8, 0.3, 0.3, 0.3], [0.3, 0.3, 0.4, 0.4, 0.4, 0.6]]
C5=[[0.3, 0.4, 0.4, 0.5, 0.5, 0.6], [0.3, 0.3, 0.4, 0.3, 0.5, 0.5], [0.8, 0.8, 0.9, 0.0, 0.2, 0.2]]
C5_=[[0.1, 0.2, 0.3, 0.5, 0.6, 0.7], [0.2, 0.3, 0.6, 0.4, 0.5, 0.5], [0.6, 0.7, 0.7, 0.3, 0.3, 0.3]]
C6=[[0.8, 0.8, 0.9, 0.0, 0.2, 0.2], [0.3, 0.4, 0.4, 0.3, 0.4, 0.6], [0.3, 0.3, 0.4, 0.3, 0.4, 0.6]]
C6_=[[0.1, 0.1, 0.3, 0.5, 0.6, 0.6], [0.5, 0.6, 0.7, 0.2, 0.2, 0.4], [0.4, 0.4, 0.4, 0.3, 0.5, 0.5]]
C7=[[0.3, 0.3, 0.4, 0.3, 0.5, 0.6], [0.3, 0.4, 0.6, 0.4, 0.4, 0.5], [0.7, 0.8, 0.9, 0.0, 0.1, 0.1]]
C7_=[[0.2, 0.2, 0.4, 0.5, 0.6, 0.8], [0.5, 0.6, 0.6, 0.2, 0.3, 0.3], [0.3, 0.4, 0.5, 0.4, 0.5, 0.6]]
C8=[[0.7, 0.8, 0.9, 0.0, 0.1, 0.2], [0.3, 0.3, 0.4, 0.3, 0.5, 0.6], [0.3, 0.4, 0.5, 0.4, 0.5, 0.5]]
C8_=[[0.1, 0.3, 0.4, 0.5, 0.7, 0.7], [0.5, 0.7, 0.8, 0.2, 0.3, 0.3], [0.2, 0.3, 0.4, 0.3, 0.4, 0.5]]
C9=[[0.8, 0.8, 0.9, 0.0, 0.1, 0.2], [0.3, 0.4, 0.4, 0.3, 0.5, 0.6], [0.3, 0.4, 0.6, 0.4, 0.5, 0.5]]
C9_=[[0.1, 0.1, 0.2, 0.4, 0.5, 0.6], [0.3, 0.4, 0.4, 0.4, 0.5, 0.6], [0.5, 0.6, 0.8, 0.2, 0.3, 0.4]]
C10=[[0.7, 0.8, 0.9, 0.0, 0.1, 0.2], [0.2, 0.5, 0.6, 0.4, 0.5, 0.5], [0.2, 0.5, 0.6, 0.5, 0.5, 0.6]]
C10_=[[0.3, 0.3, 0.4, 0.3, 0.5, 0.6], [0.5, 0.6, 0.6, 0.3, 0.3, 0.3], [0.2, 0.2, 0.3, 0.7, 0.7, 0.8]]
C11=[[0.6, 0.7, 0.9, 0.1, 0.1, 0.2], [0.2, 0.4, 0.5, 0.4, 0.4, 0.5], [0.3, 0.3, 0.4, 0.4, 0.5, 0.6]]
C11_=[[0.1, 0.1, 0.1, 0.5, 0.5, 0.6], [0.6, 0.7, 0.7, 0.2, 0.3, 0.3], [0.3, 0.3, 0.4, 0.4, 0.4, 0.6]]
C12=[[0.7, 0.8, 0.9, 0.0, 0.1, 0.2], [0.3, 0.4, 0.6, 0.3, 0.5, 0.6], [0.2, 0.4, 0.6, 0.3, 0.5, 0.6]]
C12_=[[0.1, 0.1, 0.1, 0.5, 0.6, 0.7], [0.4, 0.4, 0.4, 0.4, 0.5, 0.6], [0.5, 0.6, 0.7, 0.2, 0.3, 0.3]]
C13=[[0.2, 0.4, 0.6, 0.3, 0.5, 0.5], [0.3, 0.4, 0.5, 0.3, 0.4, 0.5], [0.8, 0.8, 0.8, 0.0, 0.1, 0.2]]
C13_=[[0.0, 0.1, 0.1, 0.5, 0.5, 0.7], [0.6, 0.7, 0.8, 0.3, 0.3, 0.3], [0.2, 0.3, 0.4, 0.4, 0.4, 0.6]]
C14=[[0.6, 0.7, 0.9, 0.0, 0.1, 0.2], [0.4, 0.4, 0.5, 0.4, 0.4, 0.5], [0.3, 0.3, 0.4, 0.4, 0.5, 0.6]]
C14_=[[0.1, 0.1, 0.4, 0.6, 0.6, 0.7], [0.5, 0.6, 0.8, 0.2, 0.3, 0.3], [0.3, 0.3, 0.4, 0.4, 0.5, 0.6]]
C15=[[0.7, 0.8, 0.8, 0.1, 0.2, 0.2], [0.4, 0.4, 0.4, 0.4, 0.4, 0.5], [0.3, 0.5, 0.6, 0.5, 0.5, 0.5]]
C15_=[[0.0, 0.2, 0.2, 0.6, 0.6, 0.7], [0.5, 0.6, 0.6, 0.2, 0.2, 0.3], [0.2, 0.4, 0.5, 0.5, 0.5, 0.5]]
C16=[[0.4, 0.4, 0.4, 0.3, 0.5, 0.6], [0.3, 0.4, 0.4, 0.3, 0.4, 0.5], [0.7, 0.8, 0.8, 0.1, 0.2, 0.2]]
C16_=[[0.0, 0.2, 0.3, 0.5, 0.6, 0.7], [0.2, 0.4, 0.6, 0.3, 0.4, 0.6], [0.5, 0.5, 0.6, 0.3, 0.3, 0.3]]
C17=[[0.3, 0.3, 0.4, 0.4, 0.5, 0.6], [0.4, 0.4, 0.4, 0.3, 0.4, 0.5], [0.7, 0.8, 0.8, 0.0, 0.2, 0.2]]
C17_=[[0.0, 0.3, 0.3, 0.5, 0.5, 0.7], [0.2, 0.4, 0.6, 0.5, 0.5, 0.6], [0.6, 0.6, 0.7, 0.3, 0.3, 0.4]]
C18=[[0.7, 0.8, 0.9, 0.0, 0.1, 0.2], [0.3, 0.4, 0.5, 0.3, 0.5, 0.6], [0.3, 0.4, 0.6, 0.3, 0.4, 0.6]]
C18_=[[0.1, 0.2, 0.3, 0.5, 0.6, 0.7], [0.5, 0.6, 0.7, 0.3, 0.3, 0.4], [0.3, 0.3, 0.4, 0.4, 0.4, 0.6]]
C19=[[0.4, 0.4, 0.4, 0.5, 0.5, 0.6], [0.3, 0.4, 0.6, 0.4, 0.5, 0.5], [0.8, 0.8, 0.8, 0.0, 0.1, 0.2]]
C19_=[[0.2, 0.3, 0.4, 0.4, 0.5, 0.6], [0.6, 0.6, 0.7, 0.3, 0.3, 0.3], [0.0, 0.1, 0.1, 0.5, 0.5, 0.7]]
C20=[[0.7, 0.8, 0.8, 0.0, 0.1, 0.2], [0.3, 0.4, 0.4, 0.4, 0.5, 0.5], [0.4, 0.4, 0.5, 0.4, 0.4, 0.6]]
C20_=[[0.1, 0.2, 0.4, 0.5, 0.7, 0.8], [0.6, 0.6, 0.7, 0.2, 0.3, 0.3], [0.2, 0.3, 0.4, 0.4, 0.5, 0.5]]
C21=[[0.7, 0.7, 0.9, 0.0, 0.1, 0.1], [0.4, 0.4, 0.6, 0.5, 0.5, 0.5], [0.3, 0.4, 0.5, 0.4, 0.5, 0.6]]
C21_=[[0.3, 0.3, 0.4, 0.3, 0.5, 0.5], [0.6, 0.6, 0.8, 0.3, 0.3, 0.4], [0.1, 0.2, 0.3, 0.4, 0.6, 0.7]]
