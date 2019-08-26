# -*-coding:utf-8-*-
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

"""
中立评论数量时间走势预测

"""


x = range(15)
y0=[2,67,404,950,898,591,520,360,411,253,207,241,278,39,nan]
y1=[0,0,493.2524472,966.6066457,752.2269691,610.7843435,475.3210186
,385.94553
,300.3482726
,243.8732324
,189.7856002
,154.0998635
,119.9226943
,97.37340868
,75.77736446
]
plt.plot(x, y0, marker='*', mec='r', mfc='w',label=u"实际数量",linewidth=3)
plt.plot(x, y1,'b--', ms=10,label=u"预测数量",linewidth=3)

plt.xticks(x,("4.30" ,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.1,5.11,5.12,5.13,5.14))
plt.xlabel(u'日期')
plt.rc("font",size=20)
plt.ylabel(u'数量（条）')
plt.legend()
plt.show()
