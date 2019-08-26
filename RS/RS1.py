#-*-coding:utf-8-*-
import  numpy as np
import pickle as p
f= open('data_array.p','rb')
data_array=p.load(f)

'''
n,m=data_array.shape
print "[",
for i in range(n):
    print "[",
    for j in range(m):
        print int(data_array[i][j]),
        print ",",
    print "],"
print "],",
'''


data_array111=[
[ 2 , 1 , 1 , 2 , 3 , 2 , 1 , 2 , 1 , 2 , 1 , 1 , 2 , 1 , 3 , 2 , 1 , ],
[ 3 , 1 , 2 , 1 , 3 , 2 , 1 , 2 , 1 , 2 , 1 , 1 , 2 , 1 , 3 , 2 , 2 , ],
[ 3 , 2 , 1 , 2 , 2 , 1 , 2 , 3 , 3 , 3 , 1 , 3 , 2 , 1 , 2 , 3 , 3 , ],
[ 1 , 1 , 1 , 3 , 3 , 3 , 2 , 3 , 3 , 3 , 1 , 1 , 1 , 1 , 2 , 2 , 1 , ],
[ 3 , 1 , 3 , 3 , 2 , 1 , 2 , 3 , 3 , 2 , 1 , 1 , 3 , 1 , 1 , 1 , 3 , ],
[ 1 , 1 , 1 , 1 , 2 , 1 , 1 , 2 , 3 , 3 , 2 , 2 , 2 , 1 , 2 , 1 , 3 , ],
[ 3 , 2 , 1 , 2 , 2 , 1 , 2 , 3 , 1 , 1 , 1 , 2 , 2 , 1 , 2 , 3 , 2 , ],
[ 2 , 1 , 2 , 2 , 1 , 2 , 1 , 1 , 3 , 2 , 1 , 1 , 2 , 3 , 1 , 2 , 2 , ],
[ 2 , 1 , 2 , 2 , 1 , 2 , 1 , 1 , 3 , 2 , 1 , 1 , 2 , 2 , 2 , 3 , 1 , ],
[ 1 , 2 , 1 , 1 , 2 , 3 , 3 , 3 , 2 , 2 , 1 , 2 , 2 , 3 , 3 , 3 , 3 , ],
[ 2 , 1 , 1 , 1 , 2 , 3 , 2 , 1 , 1 , 1 , 1 , 3 , 2 , 1 , 3 , 3 , 1 , ],
[ 2 , 1 , 1 , 1 , 2 , 2 , 1 , 1 , 1 , 1 , 1 , 3 , 2 , 1 , 2 , 3 , 2 , ],
[ 3 , 2 , 1 , 1 , 3 , 3 , 3 , 3 , 3 , 2 , 1 , 2 , 1 , 3 , 2 , 2 , 3 , ],
[ 3 , 1 , 2 , 1 , 2 , 3 , 3 , 3 , 3 , 2 , 3 , 1 , 3 , 3 , 1 , 2 , 2 , ],
[ 2 , 1 , 2 , 1 , 1 , 2 , 1 , 2 , 1 , 1 , 1 , 3 , 1 , 3 , 2 , 1 , 2 , ],
]

data_array11=[
[ 2 , 1 , 1 , 2 , 1 , 2 , 1 , 2 , 1 , 2 , 1 , 1 , 2 , 1 , 1 , 2 , 1 , ],
[ 3 , 1 , 2 , 3 , 1 , 2 , 1 , 2 , 1 , 2 , 1 , 1 , 2 , 1 , 1 , 2 , 2 , ],
[ 3 , 2 , 1 , 2 , 2 , 1 , 3 , 3 , 2 , 2 , 1 , 3 , 2 , 3 , 2 , 3 , 3 , ],
[ 1 , 1 , 1 , 3 , 1 , 1 , 2 , 1 , 3 , 1 , 1 , 1 , 1 , 1 , 2 , 2 , 1 , ],
[ 3 , 1 , 3 , 3 , 2 , 1 , 2 , 3 , 3 , 2 , 1 , 1 , 3 , 1 , 3 , 1 , 3 , ],
[ 1 , 1 , 1 , 1 , 2 , 1 , 3 , 2 , 3 , 3 , 2 , 2 , 3 , 2 , 2 , 1 , 3 , ],
[ 3 , 3 , 2 , 2 , 1 , 2 , 1 , 3 , 1 , 1 , 1 , 3 , 1 , 2 , 1 , 2 , 2 , ],
[ 2 , 1 , 2 , 2 , 1 , 2 , 2 , 1 , 2 , 2 , 1 , 1 , 2 , 2 , 1 , 2 , 2 , ],
[ 2 , 1,  2 , 2 , 2 , 1 , 1 , 1 , 2 , 2 , 1 , 1 , 2 , 2 , 1 , 2 , 1 , ],
[ 1 , 2 , 1 , 1 , 2 , 3 , 3 , 3 , 2 , 3 , 1 , 3 , 2 , 3 , 3 , 3 , 3 , ],
[ 2 , 1 , 1 , 1 , 2 , 2 , 2 , 1 , 2 , 2 , 1 , 1 , 2 , 2 , 1 , 2 , 1 , ],
[ 2 , 1 , 1 , 1 , 2 , 2 , 2 , 1 , 2 , 1 , 1 , 3 , 2 , 2 , 1 , 2 , 2 , ],
[ 3 , 2 , 1 , 1 , 2 , 3 , 3 , 3 , 2 , 2 , 1 , 2 , 1 , 3 , 2 , 3 , 3 , ],
[ 3 , 2 , 1 , 1 , 2 , 3 , 3 , 3 , 2 , 2 , 1 , 2 , 2 , 3 , 1 , 2 , 2 , ],
[ 3 , 2 , 1 , 1 , 2 , 3 , 3 , 3 , 2 , 2 , 1 , 2 , 1 , 3 , 2 , 1 , 2 , ],
]
data_array11=np.array(data_array11)





def ind(X):
    '''
    判断不可分辨关系
    :param X:
    :return:
    '''
    n,m=X.shape
    print(n,m)
    ss=[]
    for i in range(n):
        if X[i][0]!=0:
            s=[i]
            for j in range(i+1,n):
                if  X[j][0]!=0:
                    if sum([1 for ii,jj in zip(X[i],X[j]) if ii==jj])==m:
                        for f in range(len(X[j])):
                            X[j][f]=0
                        s.append(j)
            ss.append(s)

    return ss

def ind_bian(X,P):
    '''
    带有阈值的可变不可分辨关系划分
    判断不可分辨关系
    :param X:
    :return:
    '''
    n,m=X.shape
    print (n,m)
    ss=[]
    for i in range(n):
        if X[i][0]!=0:
            s=[i]
            for j in range(i+1,n):
                if  X[j][0]!=0:
                    if sum([1 for ii,jj in zip(X[i],X[j]) if ii==jj])>=m*P:
                        for f in range(len(X[j])):
                            X[j][f]=0
                        s.append(j)
            ss.append(s)

    return ss

def ind_D(D):
    '''

    :param D:
    :return:
    '''
    ss=[]
    for i in range(len(D)):
        if D[i]!=0:
            s=[i]
            for j in range(i+1,len(D)):
                if D[j]!=0:
                    if D[i]==D[j]:
                        s.append(j)
                        D[j]=0
            ss.append(s)
    return ss



def delete(X,index):
    '''
    删除X中下标为i的元素
    :param X:
    :param i:
    :return:
    '''
    X1=np.delete(X,index,axis=1)
    print (X1.shape)
    print (X1)


def pos(ind_C,ind_D):
    '''
    条件属性C下的正域
    :param ind_C:
    :param ind_D:
    :return:
    '''
    ss=[]
    for line in ind_C:
        for line1 in ind_D:
            if sum([1 for i in line if i in line1])==len(line):
                ss+=line
    return ss
def CshuyuD(C,D):
    '''
    判断列表C是否完全属于D
    :param C:
    :param D:
    :return:
    '''
    if sum([1 for i in C if i in D])!=len(C) and sum([1 for i in C if i in D])!=0:
        return True
    else:
        return False
import math
def xinxishang(ind_C,ind_D):
    '''
    '''
    U=15.0
    s=[]
    for ele in ind_C:
        for ele1 in ind_D:
            if CshuyuD(ele,ele1)==True:
                X_Y=sum([1 for i in ele if i in ele1])#即属于C又属于D的元素个数
                X=len(ele)
                s.append((X_Y,X))
    sss=0.0
    for line in s:
        print ("%d/%d*log(%d/%d)"%(line[0],U,line[0],line[1]))
        ss=-(float(line[1])/U)*(float(line[0])/float(line[1]))*math.log10((float(line[0])/float(line[1])))

        sss+=ss
    print(sss)



'''
#print data_array1[:][-1]
ind_D=ind_D(data_array1[:][-1])
C=data_array11
C1=data_array11[:,0:4]
ind_C=ind(C1)
pos_CD=pos(ind_C,ind_D)
print pos_CD,len(pos_CD)
#C1-{1}
C1_1=np.delete(C1,2,axis=1)
ind_C1_1=ind(C1_1)
pos_C1_1D=pos(ind_C1_1,ind_D)
print pos_C1_1D,len(pos_C1_1D)
'''
AC=data_array11[:]
AC=AC[:,:-1]
#AC=data_array11[:,:-1]
C=data_array11[:]
C=C[:,:-1]
#C=data_array11[:,:-1]
D=data_array11[:,-1]

ind_C=ind(C)
ind_D=ind_D(D)

pos_CD=pos(ind_C,ind_D)
#print pos_CD,len(pos_CD)




C1=AC[:,4:8]
ind_C1=ind(C1)
print("ind_C1" ,ind_C1)
#print ind_D
posC1D=pos(ind_C1,ind_D)

print (posC1D,len(posC1D))
C1_1=np.delete(C1,3,axis=1)
ind_C1_1=ind(C1_1)
print (ind_C1_1)
posC1_1D=pos(ind_C1_1,ind_D)
print (posC1_1D,len(posC1_1D))
xinxishang(ind_C1,ind_D)




'''
s1=[0,1,2,3]
s2=[4,5,6,7]
s3=[8,9,10,11]
s4=[12,13,14,15]
m,n=AC.shape


C_1=np.delete(AC,s4,axis=1)
ind_C_1=ind_bian(C_1,1.0)
print ind_C_1
pos_C_1D=pos(ind_C_1,ind_D)
print pos_C_1D,len(pos_C_1D)

xinxishang(ind_C_1,ind_D)

#print ind_C1
#ind(data_array1[:,0:3])


'''
