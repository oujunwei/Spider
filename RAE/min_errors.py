#-*-coding:utf-8-*-
import numpy as np

def min_errors(self,tree_list):
        length=len(tree_list)
        length1=len(tree_list[0].data)
        error_list=[]
        indx=0
        vec1=np.zeros((1,length1))
        vec2=np.zeros((1,length1))
        for i in range(0,length-1):
            vec1[0,:]=tree_list[i].data[:]
            n1=tree_list[i].yezi_num(tree_list[i])
            vec2[0,:]=tree_list[i+1].data[:]
            n2=tree_list[i+1].yezi_num(tree_list[i+1])
            error=self.error_rec(vec1,vec2,n1,n2)
            error_list.append(error)
            tree_list[i].s=0
            tree_list[i+1].s=0
        for j in range(len(error_list)-1):
                if error_list[j]>error_list[j+1]:
                    indx=j+1
        return indx