# 导包
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# TODO 1. numpy 准备数据
# 模拟半年的销量数据
months = np.array([i for i in range(1, 13)])
sales = np.array([random.randint(0, 500) for i in months])
print(months)
# TODO 2. 分析数据
df = pd.DataFrame({'月份': months, '销量': sales})
print(df)

# TODO 3. 绘制折线图
# 可以在这里修改样式
# plt.plot(df['月份'], df['销量'])
plt.plot(df['月份'], df['销量'],
         color='pink',
         linestyle='-',
         marker='o',
         markerfacecolor='white',
         markeredgecolor='red',
         markersize=5
         )

# 添加标题
plt.title('2025年销量折线图')
# 添加网格
plt.grid()
plt.xticks(months)
# 添加x, y轴标签
plt.xlabel('月份')
plt.ylabel('销量')
plt.show()
