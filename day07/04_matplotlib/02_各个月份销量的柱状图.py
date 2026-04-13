# 导包
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

import matplotlib

matplotlib.use('TkAgg')

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 准备数据
months = np.array([i for i in range(1, 13)])
sales = np.array([random.randint(0, 500) for i in months])
print(months)

# 2. 数据表格
df = pd.DataFrame({'月份': months, '销量': sales})
print(df)

# 3. 绘制柱状图
plt.figure(figsize=(10, 5))

# 柱状图 正确样式（去掉了折线图才有的参数）
bars = plt.bar(df['月份'], df['销量'],
               color='pink',  # 柱子颜色
               edgecolor='blue',  # 柱子边框色
               linewidth=1,  # 边框粗细
               label='月度销量'  # 图例名称
               )

# 标题改成柱状图（更准确）
plt.title('2025年销量柱状图')
plt.grid(axis='y', alpha=0.3)  # 只显示水平网格，更清爽
plt.xticks(months)
plt.xlabel('月份')
plt.ylabel('销量')

# 添加图例
plt.legend(loc='best')

# 给每个柱子添加标签
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
             str(bar.get_height()), ha='center', va='bottom', color='red', fontweight='bold')
plt.show()
