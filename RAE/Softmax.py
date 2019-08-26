# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt
import copy
from scipy.linalg import norm
from math import pow
from scipy.optimize import fminbound,minimize
import random
import jieba
from gensim.models.word2vec import *
model=Word2Vec.load('total1_50.txt')

#from gensim_word2vec import RAE
from RAE_train import RAE
import decimal
#向量点乘
def _dot(a, b):
    mat_dot = np.dot(a, b)
    return np.exp(mat_dot)

def condProb(theta, thetai, xi):
    numerator = _dot(thetai, xi.transpose())

    denominator = _dot(theta, xi.transpose())
    denominator = np.sum(denominator, axis=0)
    p = numerator / denominator
    return p
#损失函数
def costFunc(alfa, *args):
    i = args[2]
    original_thetai = args[0]
    delta_thetai = args[1]
    x = args[3]
    y = args[4]
    lamta = args[5]

    labels = set(y)
    thetai = original_thetai
    thetai[i, :] = thetai[i, :] - alfa * delta_thetai
    k = 0
    sum_log_p = 0.0
    for label in labels:
        index = y == label
        xi = x[index]
        p = condProb(original_thetai,thetai[k, :], xi)
        log_p = np.log10(p)
        sum_log_p = sum_log_p + log_p.sum()
        k = k + 1
    r = -sum_log_p / x.shape[0]+ (lamta / 2.0) * pow(norm(thetai),2)
    #print r ,alfa

    return r



class Softmax:
    def __init__(self, alfa, lamda, feature_num, label_mum, run_times, col = 1e-6):
        self.alfa = alfa
        self.lamda = lamda
        self.feature_num = feature_num
        self.label_num = label_mum
        self.run_times = run_times
        self.col = col
        self.theta = np.random.random((label_mum, feature_num+1 ))+1.0
    def oneDimSearch(self, original_thetai,delta_thetai,i,x,y ,lamta):
        res = minimize(costFunc, 0.0, method = 'Powell', args =(original_thetai,delta_thetai,i,x,y ,lamta))
        return res.x
    def train(self, x, y):
        tmp = np.ones((x.shape[0], x.shape[1] + 1))
        tmp[:,1:tmp.shape[1]] = x

        x = tmp
        del tmp
        labels = set(y)
        self.errors = []
        old_alfa = self.alfa

        for kk in range(0, self.run_times):
            print '第',kk,'次迭代'
            i=0
            for label in labels:
                tmp_theta = copy.deepcopy(self.theta)
                one = np.zeros(x.shape[0])
                index = y == label
                one[index] = 1.0
                one=np.array([one])
                thetai = np.array([self.theta[i, :]])
                prob = self.condProb(thetai, x)
                prob =one - prob
                delta_thetai = - np.dot(prob,x) / x.shape[0] + self.lamda * self.theta[i, :]
                self.theta[i,:] = tmp_theta[i,:] - self.alfa *delta_thetai
                i=i+1
        print '训练完成'


    def performance(self, tmp_theta):
        return norm(self.theta - tmp_theta)
    def dot(self, a, b):
        mat_dot = np.dot(a, b)
        return np.exp(mat_dot)
    def condProb(self, thetai, xi):
        numerator = self.dot(thetai, xi.transpose())
        denominator = self.dot(self.theta, xi.transpose())
        denominator = np.sum(denominator, axis=0)
        p = numerator[0]/ denominator
        return p
    def predict(self, x):
        tmp = np.ones((x.shape[0], x.shape[1] + 1))
        tmp[:,1:tmp.shape[1]] = x
        x = tmp
        row = x.shape[0]#样本数
        col = self.theta.shape[0]#类别数
        pre_res = np.zeros((row, col))
        #每个样本在每个类别下的概率
        for i in range(0, row):
            xi = x[i, :]
            for j in range(0, col):
                thetai = self.theta[j, :]
                p = self.condProb(np.array([thetai]), np.array([xi]))
                pre_res[i, j] = p
        r = []
        for i in range(0, row):
            tmp = []
            line = pre_res[i, :]
            ind = line.argmax()

            tmp.append(1-ind)
            tmp.append(line[ind])
            r.append(tmp)
        return np.array(r)



def clearBOM(filePath):
     fp = open(filePath,'rb+')
     if "\xef\xbb\xbf" == fp.read(3):
         contents = fp.read()
         fp.seek(0)
         fp.write(contents)
         print("Clear " + filePath + " UTF-8 BOM succ");
     fp.close()
     return True
def list2vec(list):
    m=len(list)
    n=list[0].shape[1]
    vec=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            s=round(list[i][0,j],2)
            vec[i,j]=s
    return vec

def listlist_vec(list):
    m=len(list)
    n=len(list[0])
    vec=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            s=list[i][j]
            vec[i,j]=s
    return vec

def buildWordVector(text,size):
    vec=np.zeros(size).reshape((1,size))
    count=0.
    for word in text:
        try:
            vec +=model[word].reshape((1,size))
            count +=1
        except KeyError:
            continue
    if count !=0:
        vec /=count
    return vec

def load(name,rae):
    x =[]
    y =[]
    result=np.zeros((1,50))
    i=0
    for line in open(name, 'r'):
        ele = line.split(' ')
        #print '正在训练第',i ,'个句子向量'
        vec=buildWordVector(ele,50)
        x.append(vec)
        try:
            result,s1,x2,r4,r5=rae.tree_creat(ele[0])
            result3=result.data
            #result3=rae.sentiment_sentencevec(ele[0])
            #result3=rae.sentence_vec(ele[0])
            #x.append(result3)
        except:
            print 'error word',i,line


        try:
            y.append(ele[1])
        except:
            print 'error y',i
        i=i+1
        result=np.zeros((1,50))
    #vec1=list2vec(x)
    vec1=listlist_vec(x)
    return [vec1, y]

if __name__ == '__main__':
    #[x, y] = samples(1000, 2, 5)
    #save('data.txt', x, y)
    list=[]
    for i in range(1):
        print '正在第',i,'次训练'
        rae=RAE(50)
        rae.train_weight3()
        clearBOM('F://softmax_test_data/train_data.txt')
        clearBOM('F://COAE_data/train_data.txt')
        clearBOM('F://COAE_data/test_data1.txt')
       # [x, y] = load('F://COAE_data/train_data1.txt',rae)
        #[x1, y1] = load('F://COAE_data/test_data4.txt',rae)
        #[x1, y1] = load('F://COAE_data/test_data2.txt',rae)


        clearBOM('D://new_data/train_data.txt')
        clearBOM('D://new_data/train_data.txt')
        clearBOM('D://new_data/test_data.txt')
        [x, y] = load('D://new_data/train_data.txt',rae)
        #[x1, y1] = load('F://COAE_data/test_data4.txt',rae)
        [x1, y1] = load('D://new_data/test_data.txt',rae)

        #result=open('D://SVM/SVM/traindata1.txt','w')
        #result1=open('D://SVM/SVM/testdata1.txt','w')

        index= range(0, x.shape[0])
        index1=range(0,x1.shape[0])
        #random.shuffle(index)
        x = np.array(x)
        y = np.array(y)
        x1 = np.array(x1)
        y1 = np.array(y1)

        x_train = x[index[0:3577],:]
        y_train = y[index[0:3577]]
        softmax = Softmax(0.4, 0.01, 50, 2,100)
        softmax.train(x_train, y_train)

        #[x1, y1] = load('F://softmax_test_data/train_data.txt')

        x_test=x[index[0:3577],:]
        y_test=y[index[0:3577]]
        r=softmax.predict(x_test)
        print r
