# -*-coding:utf-8-*-
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

"""
"医院医生”时间序列情感分布

"""


x = range(14)
y0=[0,1,3,7,2,6,9,3,3,1,2,3,1,0,]
y1=[0,7,63,153,139,130,96,84,61,91,65,64,65,9]
y2=[0,20,132,299,330,258,201,158,115,176,147,95,114,14]
plt.plot(x, y0, marker='o', mec='r', mfc='w',label=u"正面评论",linewidth=3)
plt.plot(x, y1, marker='*', ms=10,label=u"中立评论",linewidth=3)
plt.plot(x, y2, marker='+', ms=10,label=u"负面评论",linewidth=3)
plt.xticks(x,("4.30" ,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.1,5.11,5.12,5.13))
plt.xlabel(u'日期')
plt.rc("font",size=20)
plt.ylabel(u'数量（条）')
plt.legend()
plt.show()
