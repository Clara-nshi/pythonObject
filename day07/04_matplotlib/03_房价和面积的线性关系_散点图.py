# 导包
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 使用 numpy 准备数据
# 模拟 50 个房屋面积数据
my_array = np.random.randint(50, 100, 50)
print(my_array)
# 模拟预测房价的数据
my_predict = my_array*2 + np.random.randint(10, 200, 50)

# pandas 分析数据
df = pd.DataFrame({'面积': my_array, '预测房价': my_predict})
print(df)

# 通过matplotlib绘制散点图
plt.scatter(df['面积'], df['预测房价'], color='red', alpha=0.5)
plt.title('房屋面积和预测房价散点图')
plt.xlabel('面积')
plt.ylabel('预测房价')
plt.show()
