#!/usr/bin/env python
# coding: utf-8
from pylab import *

import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

'''
means1= (0,3,3,21,16,18,20,8,8,3,4,5,12,0)
means2 = (2,67,404,950,898,591,520,360,411,253,207,241,278,39)
means3 = (1,77,551,1341,1541,905,801,557,520,457,346,310,389,56)
n_groups = len(means1)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.4
rects1 = plt.bar(index, means1, bar_width,alpha=opacity, color='b',label= u"正面评论")
rects2 = plt.bar(index + bar_width, means2, bar_width,alpha=opacity,color='r',label=u'中立评论')
rects3 = plt.bar(index + bar_width+bar_width, means3, bar_width,alpha=opacity,color='g',label=u'负面评论')

#plt.xlabel('Group')
plt.ylabel(u'数量(条)')
plt.xlabel(u"日期")
plt.rc("font",size=20)

#plt.title('Scores by group and gender')
plt.xticks(index + 2*bar_width, ("4.30" ,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.1,5.11,5.12,5.13))
plt.ylim(0,1700)
plt.legend()

plt.tight_layout()
plt.show()
'''

x = range(14)
y0=[0,3,3,21,16,18,20,8,8,3,4,5,12,0]
y1=[2,67,404,950,898,591,520,360,411,253,207,241,278,39]
y2=[1,77,551,1341,1541,905,801,557,520,457,346,310,389,56]
plt.plot(x, y0, marker='o', mec='r', mfc='w',label=u"正面评论",linewidth=3)
plt.plot(x, y1, marker='*', ms=10,label=u"中立评论",linewidth=3)
plt.plot(x, y2, marker='+', ms=10,label=u"负面评论",linewidth=3)
plt.xticks(x,("4.30" ,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.1,5.11,5.12,5.13))
plt.xlabel(u'日期')
plt.rc("font",size=20)
plt.ylabel(u'数量（条）')
plt.legend()
plt.show()