# -*-coding:utf-8-*-
import matplotlib.pyplot as plt     # 导入模块
 
squares = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]         # 指定列表Y坐标为列表中的值
input_values = [0,17,98,266,328,156,130,107,165,31,38,26,27,2]
plt.plot(input_values,squares,linewidth=5)           # linewidth决定绘制线条的粗细
 
plt.title('Square Numbers',fontsize=24)     # 标题
plt.xlabel('Vaule',fontsize=14)
plt.ylabel('Square of Vaule',fontsize=14)
squares1=[5,6,7,8,9]
input_values1=[2,3,4,5,6]
plt.plot(input_values1,squares1,linewidth=5)           # linewidth决定绘制线条的粗细


plt.tick_params(axis='both',labelsize=14)      # 刻度加粗
plt.show()                  # 输出图像