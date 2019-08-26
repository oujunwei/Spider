#-*-coding:utf-8-*-
import numpy as np

def hebing(self,word1_vec,word2_vec):
        l=word1_vec.shape[1]
        word_vec=self.link(word1_vec,word2_vec)
        part1=np.dot(self.w1,word_vec.T)
        part1=part1.T
        part2=part1+self.b1
        part2=part2/100
        p=self.tanh_vec(part2)
        return p