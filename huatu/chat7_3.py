# -*-coding:utf-8-*-
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

"""
负面评论数量时间走势预测

"""


x = range(15)
y0=[1
,77
,551
,1341
,1541
,905
,801
,557
,520
,457
,346
,310
,389
,56
,nan]
y1=[0
,0
,612.5580821
,1370.634066
,1404.375989
,865.7145139
,887.026455
,546.7992063
,560.2601709
,345.3671703
,353.869332
,218.1394577
,223.5095598
,137.7803888
,141.1722316

]
plt.plot(x, y0, marker='*', mec='r', mfc='w',label=u"实际数量",linewidth=3)
plt.plot(x, y1,'b--', ms=10,label=u"预测数量",linewidth=3)

plt.xticks(x,("4.30" ,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.1,5.11,5.12,5.13,5.14))
plt.xlabel(u'日期')
plt.rc("font",size=20)
plt.ylabel(u'数量（条）')
plt.legend()
plt.show()
