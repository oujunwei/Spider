# -*-coding:utf-8-*-
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

"""
"莆田系医院”时间序列情感分布

"""


x = range(14)
y0=[0,1,0,3,0,2,2,2,0,0,0,0,0,0]
y1=[1,11,56,152,159,89,55,56,43,26,29,18,33,1]
y2=[0,17,98,266,328,156,130,107,165,31,38,26,27,2]
plt.plot(x, y0, marker='o', mec='r', mfc='w',label=u"正面评论",linewidth=3)
plt.plot(x, y1, marker='*', ms=10,label=u"中立评论",linewidth=3)
plt.plot(x, y2, marker='+', ms=10,label=u"负面评论",linewidth=3)
plt.xticks(x,("4.30" ,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.1,5.11,5.12,5.13))
plt.xlabel(u'日期')
plt.rc("font",size=20)
plt.ylabel(u'数量（条）')
plt.legend()
plt.show()
