#!/usr/bin/env python
# coding: utf-8
from pylab import *

import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
n_groups = 4
means1= (10, 46, 24, 41)
means2 = (729, 1945, 1520, 1028)
means3 = (1391, 2414, 1992, 2059)

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.4
rects1 = plt.bar(index, means1, bar_width,alpha=opacity, color='b',label= u"正面评论")
rects2 = plt.bar(index + bar_width, means2, bar_width,alpha=opacity,color='r',label=u'中立评论')
rects3 = plt.bar(index + bar_width+bar_width, means3, bar_width,alpha=opacity,color='g',label=u'负面评论')

#plt.xlabel('Group')
plt.ylabel(u'数量（条）')
#plt.title('Scores by group and gender')
plt.xticks(index + 2*bar_width, (u'莆田系医院', u'百度', u'中国社会', u'医院医生'))
plt.ylim(0,2500)
plt.legend()
plt.xlabel(u'主题')
plt.rc("font",size=20)
plt.tight_layout()
plt.show()