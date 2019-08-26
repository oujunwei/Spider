# -*-coding:utf-8-*-
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

"""
"百度”时间序列情感分布

"""


x = range(14)
y0=[0,0,0,10,13,6,4,0,3,1,1,1,7,0]
y1=[0,38,228,473,386,225,143,111,83,52,52,70,69,15]
y2=[0,32,245,538,549,273,220,99,104,88,68,97,79,20]
plt.plot(x, y0, marker='o', mec='r', mfc='w',label=u"正面评论",linewidth=3)
plt.plot(x, y1, marker='*', ms=10,label=u"中立评论",linewidth=3)
plt.plot(x, y2, marker='+', ms=10,label=u"负面评论",linewidth=3)
plt.xticks(x,("4.30" ,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.1,5.11,5.12,5.13))
plt.xlabel(u'日期')
plt.rc("font",size=20)
plt.ylabel(u'数量（条）')
plt.legend()
plt.show()
