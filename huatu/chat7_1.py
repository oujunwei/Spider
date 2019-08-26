# -*-coding:utf-8-*-
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

"""
评论数量时间走势预测

"""


x = range(15)
y0=[3,147,958,2312,2455,1514,1341,925,939,713,557,556,679,95,nan]
y1=[0,0,1129,2349,2168,1486,1372,940,940,595,549,376,347,150,103]
plt.plot(x, y0, marker='+', mec='r', mfc='w',label=u"实际数量",linewidth=3)
plt.plot(x, y1,'b*--', ms=10,label=u"预测数量",linewidth=3,)

plt.xticks(x,("4.30" ,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.1,5.11,5.12,5.13,5.14))
plt.xlabel(u'日期')
plt.rc("font",size=20)
plt.ylabel(u'数量（条）')
plt.legend()
plt.show()
