# -*- coding: utf-8 -*-
import math
import numpy as np
import jieba
from gensim.models.word2vec import *
from gensim.models.word2vec import LineSentence
from min_errors import min_errors
model=Word2Vec.load('total1_50.txt')
class TreeNode(object):
    s=0
    def __init__(self, left=0, right=0, data=0):
        self.left = left
        self.right = right
        self.data = data

    def isyezi(self,tree):
        flag=0
        if tree.left is None and tree.right is None:
            flag=1
        return flag

    def yezi_num(self,tree):
        if tree is not None:
            if self.isyezi(tree) ==1:
                self.s=self.s+1
            else:
                self.yezi_num(tree.left)
                self.yezi_num(tree.right)
        return self.s

class BTree(object):

    def __init__(self, root=0):
        self.root = root

class RAE:
    def __init__(self,size):
        self.size=size
        self.num=2
        self.w1=np.random.random((self.size,2*self.size))
        self.w2=np.random.random((self.size,2*self.size))
        self.b1=np.random.random((1,50))+1.0
        self.b2=np.random.random((1,100))+1.0
        self.run_times=200
        self.alfe=0.4
        self.l=0.5
        self.w3= np.random.random((self.num, 50 ))+1.0
        self.w_f=random.uniform(0,1)
        self.w4=np.random.random((50,100))
        self.w5=np.random.random((1,50))

    def wordlinkword(self,word1_vec,word2_vec):
        word_vec=np.zeros((1,50))
        for i in range(word_vec.shape[1]):
            word_vec[0,i]=(word1_vec[0,i]+word2_vec[0,i])/2
        return word_vec
    def link(self,x1,x2):
        length=x1.shape[1]+x2.shape[1]
        xx=np.zeros((1,length))
        xx[0,0:x1.shape[1]]=x1
        xx[0,x1.shape[1]:length]=x2
        return xx
    def tanh_vec(self,xx):
        xx_result=np.zeros((1,xx.shape[1]))
        for i in range(xx.shape[1]):
            xx1=xx[0,i]

            xx1_tanh=math.tanh(xx1)
            xx_result[0,i]=xx1_tanh
        return xx_result

    def hebing(self,word1_vec,word2_vec):
        l=word1_vec.shape[1]
        word_vec=self.link(word1_vec,word2_vec)
        part1=np.dot(self.w1,word_vec.T)
        part1=part1.T
        part2=part1+self.b1
        part2=part2/100
        p=self.tanh_vec(part2)
        return p

    def fenjie(self,vec): #分解为子节点
         length=vec.shape[1]
         r=np.dot(vec,self.w2)+self.b2
         r=r/50
         return r

    def error_rec(self,vec1,vec2,n1,n2):#重构误差
        p=self.hebing(vec1,vec2)
        r=self.fenjie(p)
        c1=vec1
        c2=vec2
        c1_=r[0,0:50]
        c2_=r[0,50:100]
        part1=0
        part2=0
        c11=c1-c1_
        c22=c2-c2_
        for i in range(p.shape[1]):
            part1+=(c11[0,i] * c11[0,i])
            part2+=(c22[0,i] * c22[0,i])
        part1=math.sqrt(part1)
        part2=math.sqrt(part2)
        part3=(float(n1)/float((n1+n2)))*part1+(float(n2)/float((n1+n2)))*part2
        return part3

    def delete_vec(self,vector,index1,index2,new_vector):
        m=vector.shape[0]
        n=vector.shape[1]
        new_vec=np.zeros((m-1,n))
        new_vec[0:index1,:]=vector[0:index1,:]
        new_vec[index1,:]=new_vector
        new_vec[index1+1:m-1,:]=vector[index2+1:m,:]
        return new_vec


    def find_index(self,vectors,vec):#在原词矩阵中找出vec向量对应的下标
        index=0
        s=0
        for i in range(vectors.shape[0]):
            for j in range(vectors.shape[1]):
                if vec[0,j]==vectors[i,j]:
                     s=s+1
            if s==vectors.shape[1]:
                    index=i
            s=0
        return index

    def wordbag_list(self,words):#将中文句子的分词词包转换为list形式
        result_list=[]
        for i in words:
            result_list.append(i)
        return result_list

    def list2vec2(self,list):#将一个树节点中的data数值由列表转换为向量
        m=len(list)
        vec=np.zeros((1,m))
        for i in range(m):
            vec[0,i]=list[i]
        return vec

    def list2vec(self,list):
        m=len(list)
        n=list[0].shape[1]
        vec=np.zeros((m,n))
        for i in range(m):
            for j in range(n):
                s=list[i][j]
                vec[i,j]=s
        return vec
    def dot(self, a, b):
        mat = np.dot(a, b.T)
        return mat.T

    def link_node(self,node1,node2):#返回 向量

        list_node=np.zeros((1,len(node1.data)+len(node2.data)))
        list_node[0,0:len(node1.data)]=node1.data[:]
        list_node[0,len(node1.data):(len(node1.data)+len(node2.data))]=node2.data[:]

        return list_node
    def listlist_vec(self,list):
        m=len(list)
        n=len(list[0])
        vec=np.zeros((m,n))
        for i in range(m):
            for j in range(n):
                s=list[i][j]
                vec[i,j]=s
        return vec
    def clearBOM(self,filePath):
        fp = open(filePath,'rb+')
        if "\xef\xbb\xbf" == fp.read(3):
            contents = fp.read()
            fp.seek(0)
            fp.write(contents)
            print("Clear " + filePath + " UTF-8 BOM succ");
        fp.close()
        return True
#sofemax层读入数据
    def load(self,name):
        x =[]
        y =[]
        result=np.zeros((1,50))
        i=0
        for line in open(name, 'r'):
            ele = line.split(' ')

            try:
                #result3=rae.sentiment_sentencevec(ele[0])
                #result3=rae.sentence_vec(ele[0])
                x.append(ele[0])
            except:
                print 'error word',line
            try:
                y.append(ele[1])
            except:
                print 'error y',i
            i=i+1
            result=np.zeros((1,50))

        return [x,y]


    def ycl(self):
        self.clearBOM('F://COAE_data/train_data.txt')
        fin=open('D://new_data/test1.txt','r')
        weight1=open('F://COAE_data/wieght_w1.txt','w')
        weight2=open('F://COAE_data/wieght_w2.txt','w')
        #[x,y]=self.load('F://COAE_data/train_data.txt')
        #x_length=len(x)
        lenth=0
        i=0
        train_list=[]
        num_list=[]
        error_list=[]
        #for i in range(len(x)):
            #line1=x[i].strip()
        for line1 in fin:
            line1=line1.strip()
            words=jieba.cut(line1)
            #for i in words:

                #s=i.encode('utf-8')
                #s=s.replace('\n','')
                #ss=model[s]



                #train_list.append(ss)

            try:
                r1,r2,r3,r4,r5=self.tree_creat(line1)
            except:
                print 'error linw',line1
            #r3=self.list2vec(r2)
        #print 'r3',r3
            train_list.append(r2)
            num_list.append(r3)
            error_list.append(r5)
        return train_list,num_list,error_list
        #return train_list


    def c1_c1(self,c1,c1_,index):#c1为向量c1_为列表
        n=len(c1)
        new_c1_=np.zeros((1,n))
        if index==0:
            new_c1_[0,0:n]=c1_[0:n]
        if index==1:
            new_c1_[0,0:n]=c1_[n:2*n]
        ss=c1-new_c1_
        s=0
        for i in range(n):
            pp=ss[0,i]*ss[0,i]
            s=s+pp
        return math.sqrt(s)

    def caifeng(self,data):
        n1=np.zeros((1,50))
        n2=np.zeros((1,50))
        n1[0,:]=data[0,0:50]
        n2[0,:]=data[0,50:100]
        return n1,n2

    def new_error_vec(self,vec1,vec2,n1,n2):
        error_vec=np.zeros((1,100))
        p=self.hebing(vec1,vec2)
        r=self.fenjie(p)
        c1=vec1
        c2=vec2
        c1_=r[0,0:50]
        c2_=r[0,50:100]
        part1=0
        part2=0
        c11=c1-c1_
        c22=c2-c2_
        for i in range(error_vec.shape[1]/2):
            error_vec[0,i]=(n1/(n1+n2))*math.sqrt((c11[0,i]*c11[0,i]))
        for j in range(error_vec.shape[1]/2):
            error_vec[0,50+j]=(n2/(n1+n2))*math.sqrt((c22[0,i]*c22[0,i]))
        return error_vec



    def train_weight1(self):
        #train_list,num_list,error_list=self.ycl()
        train_list,num_list,error_list=self.ycl()
        print '正在优化.....'

        '''
        new_x=np.zeros((mm,100))
        new_y=[]
        for ii in range(mm):
            for i in range(m):
                for j in range(len(train_list[i])):
                    new_x[i,:]=train_list[i][j]#将没个句子中 将要结合的两个词语向量 组 转换为一个矩阵 该矩阵每行为一个 结构单元
                    new_y.append(y[i])
        labels = set(new_y)
        '''
        m=len(train_list)
        jj=0
        error_sum=0
        A=np.ones((1,100))
        for i in range(m):
            for j in range(len(train_list[i])):
                jj=jj+1
        mm=jj
        for kk in range(0,50):
            #for i in range(self.w1.shape[0]):
            s=np.zeros((50,100))
            n=np.zeros((50,100))
            b1_=np.zeros((1,50))
            b2_=np.zeros((1,100))
            w_f=0
            w_f_total=0

            for ii in range(m):
                for jj in range(len(train_list[ii])):
                    vec1=self.list2vec2(train_list[ii][jj][0,0:50])
                    vec2=self.list2vec2(train_list[ii][jj][0,50:100])
                    p_std=np.std(self.hebing(vec1,vec2))
                    c1_std=np.std(vec1)
                    c2_std=np.std(vec2)
                    std_error=0.2*(p_std-max(c1_std,c2_std))
                    error_vec=self.new_error_vec(vec1,vec2,num_list[ii][jj][0],num_list[ii][jj][1])+std_error

                        #w2偏导
                    p=self.hebing(vec1,vec2)
                    ww2=np.dot(p.T,error_vec)
                    n=n+ww2
                        #w1偏导
                    a=self.tanh_vec((np.dot(train_list[ii][jj],self.w1.T)+self.b1))
                    x2=1-a*a
                    #f1=std_error+x2+#f方差损失对w1求导
                    x1=np.dot(error_vec,self.w2.T)
                    x3=x1*x2
                    ww1=np.dot(x3.T,train_list[ii][jj])
                    s=s+ww1
                    #b2偏导
                    b2=error_vec
                    b2_=b2_+b2
                    #b1偏导
                    b1=x3
                    b1_=b1_+b1
                    #w_f偏导
                    w_f_total=w_f+std_error

            sss=(s/mm)+0.2*self.w1
                #print 'sss',sss
            nnn=(n/mm)+0.2*self.w2
            bb1=(b1_/mm)+0.2*self.b1
            bb2=(b2_/mm)+0.2*self.b2
            w_f_total=(w_f_total/mm)+0.2*self.w_f
            self.w1=self.w1-self.alfe*(sss)
            self.w2=self.w2-self.alfe*(nnn)
            self.b1=self.b1-self.alfe*(bb1)
            self.b2=self.b2-self.alfe*(bb2)
            self.w_f=self.w_f-self.alfe*(w_f_total)

            #print '优化的权重',self.w1
            print '第',kk,'次迭代.......'

        if kk==5:
                print '5 timw',self.w1
        if kk==10:
                print '10 time',self.w1
        if kk==20:
                print '20 times',self.w1

        print 'finish'
    def guiyi(self,vec):#归一化向量
        m=vec.shape[1]
        new_vec=np.zeros((1,m))
        s=0
        sum_s=0
        for i in range(m):
            s=vec[0,i]*vec[0,i]
            sum_s=sum_s+s
        new_s_vec=vec/(math.sqrt(sum_s))
        return new_s_vec

    def train_weight3(self):
        #train_list,num_list,error_list=self.ycl()

        print '正在优化.....'

        for kk in range(0,40):
            train_list,num_list,error_list=self.ycl()
            m=len(train_list)
            ff=0
            A=np.ones((1,100))
            for i in range(m):
                for j in range(len(train_list[i])):
                    ff=ff+1
            mm=ff
            #for i in range(self.w1.shape[0]):
            s=np.zeros((50,100))
            n=np.zeros((50,100))
            b1_=np.zeros((1,50))
            b2_=np.zeros((1,100))
            w_f=0
            w_f_total=0
            for ii in range(m):
                for jj in range(len(train_list[ii])):
                    vec1=self.list2vec2(train_list[ii][jj][0,0:50])
                    vec2=self.list2vec2(train_list[ii][jj][0,50:100])
                    p_std=np.std(self.hebing(vec1,vec2))
                    c1_std=np.std(vec1)
                    c2_std=np.std(vec2)
                    std_error=self.w_f*(p_std-max(c1_std,c2_std))
                    error_vec=self.new_error_vec(vec1,vec2,num_list[ii][jj][0],num_list[ii][jj][1])

                        #w2偏导
                    p=self.hebing(vec1,vec2)
                    ww2=np.dot(p.T,error_vec)
                    n=n+ww2
                        #w1偏导
                    a=self.tanh_vec((np.dot(train_list[ii][jj],self.w1.T)+self.b1))
                    x2=1-a*a
                    f1=std_error*np.dot(x2.T,train_list[ii][jj])#f方差损失对w1求导
                    x1=np.dot(error_vec,self.w2.T)
                    x3=x1*x2
                    ww1=np.dot(x3.T,train_list[ii][jj])
                    s=s+ww1
                    #b2偏导
                    b2=error_vec
                    b2_=b2_+b2
                    #b1偏导
                    b1=x3
                    b1_=b1_+b1
                    #w_f偏导
                    #w_f_total=w_f+std_error

            sss=(s/mm)+0.2*self.w1
                #print 'sss',sss
            nnn=(n/mm)+0.2*self.w2
            bb1=(b1_/mm)+0.2*self.b1
            bb2=(b2_/mm)+0.2*self.b2
            w_f_total=(w_f_total/mm)+0.2*self.w_f
            self.w1=self.w1-self.alfe*(sss)
            self.w2=self.w2-self.alfe*(nnn)
            self.b1=self.b1-self.alfe*(bb1)
            self.b2=self.b2-self.alfe*(bb2)
            #self.w_f=self.w_f-self.alfe*(w_f_total)

            #print '优化的权重',self.w1
            print '第',kk,'次迭代.......'

    def error_total(self,error_list):
        error_total=0
        for i in range(len(error_list)):
            error_total=error_total+error_list[i]
        return  error_total

    def link_list(self,x1,x2):
        length=len(x1)+len(x2)
        xx=np.zeros((1,length))
        for i in range(len(x1)):
            xx[0,i]=x1[i]
            xx[0,(length/2)+i]=x2[i]
        return xx

    def line_deal(self,line):
        result=[]
        result1=[]
        words=jieba.cut(line)
        for i in words:
            i=i.encode('utf-8')
            ss=model[i]
            result.append(ss)
        for j in range(len(result)-1):
            result1.append(self.link_list(result[j],result[j+1]))
        return result1

    def ycl2(self):
        self.clearBOM('F://COAE_data/train_data.txt')
        #fin=open('F://COAE_data/test1.txt','r')
        weight1=open('F://COAE_data/wieght_w1.txt','w')
        weight2=open('F://COAE_data/wieght_w2.txt','w')
        [x,y]=self.load('F://COAE_data/train_data1.txt')
        #x_length=len(x)
        lenth=0
        i=0
        train_list=[]
        num_list=[]
        error_list=[]
        for i in range(len(x)):
            line1=x[i].strip()
        #for line1 in fin:
            #line1=line1.strip()
            #r2=self.line_deal(line1)
            try:
                r1,r2,r3,r4,r5=self.tree_creat(line1)
            except:
                print '错误语句',line1,i
            #r3=self.list2vec(r2)
        #print 'r3',r3
            train_list.append(r2)
            num_list.append(r3)
            error_list.append(r5)
        return train_list,num_list,error_list,y
        #return train_list


    def train_weight2(self):
        #train_list,num_list,error_list=self.ycl()

        for kk in range(0,10):
            train_list,num_list,error_list,y=self.ycl2()
            m=len(train_list)
            jj=0
            A=np.ones((1,100))
            labels=set(y)
            for i in range(m):
                for j in range(len(train_list[i])):
                    jj=jj+1
            mm=jj
            #for i in range(self.w1.shape[0]):
            s=np.zeros((50,100))
            n=np.zeros((50,100))
            b1_=np.zeros((1,50))
            b2_=np.zeros((1,100))
            h=np.zeros((2,50))
            labels = set(y)
            i=0
            error=1
            soft1=1
            ww3=np.zeros((1,50))
            #for label in labels:
            for ii in range(m):
                for jj in range(len(train_list[ii])):
                    vec1=self.list2vec2(train_list[ii][jj][0,0:50])
                    vec2=self.list2vec2(train_list[ii][jj][0,50:100])
                    error_vec=0.5*self.new_error_vec(vec1,vec2,num_list[ii][jj][0],num_list[ii][jj][1])
                    p=self.hebing(vec1,vec2)
                    total_exp=math.exp(np.dot(self.w3[0,:],p.T))+math.exp(np.dot(self.w3[1,:],p.T))#+math.exp(np.dot(self.w3[2,:],p.T))
                    if y[ii]==1:
                        error=0.5*math.log(math.exp(np.dot(self.w3[0,:],p.T))/total_exp)
                        soft=total_exp - math.exp((np.dot(self.w3[0,:],p.T)))* math.exp((np.dot(self.w3[1,:],p.T))) #+ math.exp((np.dot(self.w3[2,:],p.T))))
                        soft1=soft/(float(total_exp)*float(total_exp))
                        ww3=self.w3[0,:]
                    if y[ii]==-1:
                        error=0.5*math.log(math.exp(np.dot(self.w3[1,:],p.T))/total_exp)
                        soft=total_exp - math.exp((np.dot(self.w3[0,:],p.T)))*( math.exp((np.dot(self.w3[1,:],p.T))))  # + math.exp((np.dot(self.w3[2,:],p.T))))
                        soft1=soft/(float(total_exp)*float(total_exp))
                        ww3=self.w3[1,:]
                    '''
                    if y[ii]==-1:
                        error=0.5*math.log(math.exp(np.dot(self.w3[2,:],p.T))/total_exp)
                        soft=total_exp - math.exp((np.dot(self.w3[0,:],p.T)))*( math.exp((np.dot(self.w3[1,:],p.T)))+ math.exp((np.dot(self.w3[2,:],p.T))))
                        soft1=soft/(float(total_exp)*float(total_exp))
                        ww3=self.w3[2,:]
                 '''


                        #w2偏导
                    p=self.hebing(vec1,vec2)
                    ww2=np.dot(p.T,error_vec)
                    n=n+ww2

                        #w1偏导


                    x1=np.dot(error_vec,self.w2.T)
                    a=self.tanh_vec((np.dot(train_list[ii][jj],self.w1.T)+self.b1))
                    x2=1-a*a
                    x3=x1*x2
                    ww1=np.dot(x3.T,train_list[ii][jj])


                    xx1=error*soft1*ww3*x2
                    xx2=np.dot(xx1.T,train_list[ii][jj])

                    s=s+(ww1+xx2)
                    #b2偏导
                    b2=error_vec
                    b2_=b2_+b2
                    #b1偏导
                    b1=x3
                    b1_=b1_+b1

                    #w3偏导
                    if y[ii]==1:
                        hh=error*soft*train_list[ii][jj]
                        h[0,:]=h[0,:]+hh
                    if y[ii]==-1:
                        hh=error*soft*train_list[ii][jj]
                        h[1,:]=h[1,:]+hh
                        '''
                    if y[ii]==-1:
                        hh=error*soft*train_list[ii][jj]
                        h[2,:]=h[2,:]+hh
                    '''




            sss=(s/mm)+0.2*self.w1
                #print 'sss',sss
            nnn=(n/mm)+0.2*self.w2
            bb1=(b1_/mm)+0.2*self.b1
            bb2=(b2_/mm)+0.2*self.b2
            hh2=(h/mm)+0.2*self.w3
            self.w1=self.w1-self.alfe*(sss)
            self.w2=self.w2-self.alfe*(nnn)
            self.b1=self.b1-self.alfe*(bb1)
            self.b2=self.b2-self.alfe*(bb2)
            self.w3=self.w3-self.alfe*(hh2)

            #print '优化的权重',self.w1
            print '第',kk,'次迭代.......'

        if kk==5:
                print '5 timw',self.w1
        if kk==10:
                print '10 time',self.w1
        if kk==20:
                print '20 times',self.w1

        print 'finish'

    def predict(self, x):
        tmp = np.ones((x.shape[0], x.shape[1] ))
        tmp[:,0:tmp.shape[1]] = x
        x = tmp
        row = x.shape[0]#样本数
        col = self.w3.shape[0]#类别数
        pre_res = np.zeros((row, col))
        #每个样本在每个类别下的概率
        for i in range(0, row):
            xi = x[i, :]
            for j in range(0, col):
                thetai = self.w3[j, :]
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


    def load_test(self,name):
        x =[]
        y =[]
        result=np.zeros((1,50))
        i=0
        for line in open(name, 'r'):
            ele = line.split(' ')
        #print '正在训练第',i ,'个句子向量'

            try:
                result,s1,x2,r4,r5=rae.tree_creat(ele[0])
                result3=result.data
            #result3=rae.sentiment_sentencevec(ele[0])
            #result3=rae.sentence_vec(ele[0])
                x.append(result3)
            except:
                print 'error word',line


            try:
                y.append(ele[1])
            except:
                print 'error y',i
            i=i+1
            result=np.zeros((1,50))
    #vec1=list2vec(x)
        vec1=self.listlist_vec(x)
        return [vec1, y]


    def condProb(self, thetai, xi):
        numerator = self.dot(thetai, xi)
        numerator=numerator.T
        denominator = self.dot(self.w3, xi)
        denominator=denominator.T
        denominator = np.sum(denominator, axis=0)
        p = numerator[0]/ denominator
        return p
    def condProb1(self, thetai, xi):
        #print 'thetai',thetai.shape[0],thetai.shape[1]
        #print 'xi',xi.shape[0],xi.shape[1]

        numerator = self.dot(thetai, xi.T)
        numerator=numerator
        denominator = self.dot(self.w3, xi)
        denominator=denominator.T
        denominator = np.sum(denominator, axis=0)
        p = numerator[0]/ denominator
        return p

    def hebing_node(self,node1,node2):#对树种两个节点中的数值data进行合并
        new_node=TreeNode(None,None,0)
        new_node.left=node1
        new_node.right=node2
        length=len(node1.data)
        vec1=np.zeros((1,length))
        vec2=np.zeros((1,length))
        new_data=[]
        for i in range(length):
            vec1[0,i]=node1.data[i]
            vec2[0,i]=node2.data[i]
        vec3=self.hebing(vec1,vec2)
        for j in range(length):
            new_data.append(vec3[0,j])

        new_node.data=new_data
        return new_node

    def new_list(self,result_list,node_new,index1,index2):
        new_list=[]
        length=len(result_list)
        result_list[index1]=node_new
        result_list[index2]=0
        for i in range(length):
            if result_list[i] != 0:
                new_list.append(result_list[i])
        return new_list
    def guiyi_list(self,list1):
        s=[]
        part1=0
        part2=0
        for i in range(len(list1)):
            part1=list1[i]*list1[i]
            part2=part2+part1
        part2=math.sqrt(part2)
        for j in range(len(list1)):
            s.append(list1[j]/part2)
        return s



    def tree_creat(self,sentence):
        words=jieba.cut(sentence)
        length=0
        flag=0
        result_list=[]#句子中词的列表
        node1=TreeNode
        node_new=TreeNode
        #将叶子节点放入列表result_list
        link_words=[]#将进行合并的节点存储
        num_list=[]#将即将合并节点的叶子树存储
        p_list=[]
        error_list=[]
        list1=[]
        for i in words:
            length=length+1
            s=i.encode('utf-8')
            s=s.replace('\n','')
            #fg=self.guiyi_list(model[s])
            fg=model[s]
            node1=TreeNode(None,None,data=fg)

            result_list.append(node1)
        if length==1:
            node_new=result_list[0]
        else:
            for j in range(length):
                if len(result_list) == 1:
                    flag=1
                else:
                    index1=min_errors(result_list)
                    index2=index1+1
                    error=self.error_rec(self.list2vec2(result_list[index1].data),self.list2vec2(result_list[index2].data),result_list[index1].yezi_num(result_list[index1]),result_list[index2].yezi_num(result_list[index2]))
                    node_new=self.hebing_node(result_list[index1],result_list[index2])
                    #list1.append(result_list[index1])
                    #list1.append(result_list[index2])
                    link_words.append(self.link_node(result_list[index1],result_list[index2]))
                    num_list.append(np.array([result_list[index1].yezi_num(result_list[index1]),result_list[index2].yezi_num(result_list[index2])]))
                    result_list=self.new_list(result_list,node_new,index1,index2)
                    p_list.append(node_new)
                    error_list.append(error)
                list1=[]
        return node_new,link_words,num_list,p_list,error_list

    def test_tree(self):
        sentence='今天天气不错适合运动'
        node_new=self.tree_creat(sentence)
    def cos_similar(self,node1,node2):
        sum_all=0
        sum_o1=0
        sum_o2=0

        for i in range(len(node1.data)):
            mul_all=node1.data[i]*node2.data[i]
            sum_all+=mul_all
            o1=node1.data[i]*node1.data[i]
            sum_o1+=o1
            o2=node2.data[i]*node2.data[i]
            sum_o2+=o2
        a=math.sqrt(sum_o1)
        b=math.sqrt(sum_o2)
        cos_result=sum_all/(a*b)
        return cos_result

    def read_lines(self,filename):
        fp = open(filename, 'r')
        lines = []
        for line in fp.readlines():
            line = line.strip()
            line = line.decode("utf-8")
            lines.append(line)
        fp.close()
        return lines

    def sentiment_sentencevec(self,sentence):
        posdict = self.read_lines("C://python27/Sentiment_dict1/Sentiment_dict/emotion_dict/pos_all_dict.txt")
        negdict = self.read_lines("C://python27/Sentiment_dict1/Sentiment_dict/emotion_dict/neg_all_dict.txt")
        inverse = self.read_lines("C://python27/Sentiment_dict1/Sentiment_dict/degree_dict/inverse.txt")

        words=list(jieba.cut(sentence))
        sentence_vec1=np.zeros((1,50))
        words_vec=np.zeros((1,50))
        w=1
        for i in range(len(words)-1):
            words[i]= words[i].encode('utf-8')
            if  words[i] in posdict:
                w=2
            if  words[i] in negdict :
                w=-2
            try:
                words_list=model[words[i]]
            except:
                print 'eroor',sentence
            for j in range(len(words_list)):

                words_vec[0,j]=w*words_list[j]
            sentence_vec1=self.wordlinkword(sentence_vec1,words_vec)
        return  sentence_vec1

    def sentence_vec(self,sentence):
        words=list(jieba.cut(sentence))
        sentence_vec1=np.zeros((1,50))
        words_vec=np.zeros((1,50))
        for i in range(len(words)-1):
            words[i]= words[i].encode('utf-8')
            try:
                words_list=model[words[i]]
            except:
                print 'eroor',i,sentence
            for j in range(len(words_list)):
                words_vec[0,j]=words_list[j]
            #words_vec=self.guiyi(words_vec)
            sentence_vec1=self.wordlinkword(sentence_vec1,words_vec)
        sentence_vec1=sentence_vec1*self.w5
        return  sentence_vec1
'''
    def tree_error(self,s):
        words=jieba.cut(s)
        i=0
        for word in words:
            i=i+1
            length=i
        vec2,link_words,num_list,p_list,error_list=rae.tree_creat(s)
        error_total=0
        j=len(link_words)
        for jj in j:
'''





if __name__ == '__main__':
    s='纯粹就是国企招待所的作风和质量整个酒店看上去显得比较陈旧'
    rae=RAE(50)
    s_vec=rae.sentence_vec(s)
    rae.train_weight3()

    w1='希望'
    w2='更多人'
    w3='知道'
    w4='这件'
    w5='事情'

    vec1=np.zeros((1,50))
    vec1[0,0:50]=model[w1]


    vec2=np.zeros((1,50))
    vec2[0,0:50]=model[w2]


    vec3=np.zeros((1,50))
    vec3[0,0:50]=model[w3]

    vec4=np.zeros((1,50))
    vec4[0,0:50]=model[w4]

    vec5=np.zeros((1,50))
    vec5[0,0:50]=model[w5]



    error1=rae.error_rec(vec1,vec2,1,1)
    error2=rae.error_rec(vec2,vec3,1,1)
    error3=rae.error_rec(vec3,vec4,1,1)
    error4=rae.error_rec(vec4,vec5,1,1)
    #error3=rae.error_rec(vec3,vec45)
   # error4=rae.error_rec(vec4,vec5)



    print 'error1',error1
    print 'error2',error2
    print 'error3',error3
    print 'error4',error4

    error_total=0
    node_new,link_words,num_list,p_list,error_list=rae.tree_creat(s)
    for i in range(len(error_list)):
        error_total=error_total+error_list[i]
    print 'error_total',error_total

    s1='有事多事之秋啊这些大品牌蒙牛修正药业酒鬼酒都该倒闭啊'
    sentence_data1,r1,s1,s4,s5=rae.tree_creat(s1)
    s2='蒙牛真果粒的牛奶饮品很好喝我特别爱'
    sentence_data2,r2,s2,s4,s5=rae.tree_creat(s2)
    s3='度的败类以前把蒙牛当做民族的骄傲现在唉所以说当真爆发了战争别国都不需要真正打中国自己人都把自己人给打死了'
    sentence_data3,r3,s3,s4,s5=rae.tree_creat(s3)
    s4='卧槽这光天化日众目睽睽之下居然发生这种事酒店应该不是第一次发生这种事吧抵制这种酒店'
    sentence_data4,r4,s4,s4,s5=rae.tree_creat(s4)


    sim1=rae.cos_similar(sentence_data1,sentence_data2)
    sim2=rae.cos_similar(sentence_data1,sentence_data3)
    sim3=rae.cos_similar(sentence_data1,sentence_data4)
    print 'sim1',sim1
    print 'sim2',sim2
    print 'sim3',sim3

    print 's_vec',s_vec
    print 's_vec_std',np.std(s_vec)
    new_s_vec=[]
    for i in range(len(sentence_data2.data)):
        new_s_vec.append(sentence_data2.data[i])
    print 'new_s_vec',new_s_vec
    print 'new_s_vec_std',np.std(new_s_vec)

    #print 'w1w1w1',rae.w1
    [x1, y1] = rae.load_test('F://COAE_data/test_data2.txt')
    index1=range(0,x1.shape[0])
    x1 = np.array(x1)
    y1 = np.array(y1)

        #[x1, y1] = load('F://softmax_test_data/train_data.txt')
    x_test=x1[index1[0:340],:]
    y_test=y1[index1[0:340]]
    r=rae.predict(x_test)
    right=0
    right1=0
    data_0=[]
    for i in range(len(y_test)):
        if int(y_test[i])*1.0==1 and r[i][0]==1:
            right=right+1
        if int (y_test[i])*1.0==-1 and r[i][0]==0:
            right1=right1+1
        if r[i][0]==0:
            data_0.append(i)

    print r
    print '测试样本类别为1',right
    print '测试样本类别为-1',right1
    s=float(right+right1)/float(len(y_test))
    print 'right level',s
        #print data_0
    print list


