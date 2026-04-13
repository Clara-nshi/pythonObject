# # 导包
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('TkAgg')
# # TODO 1. numpy 复杂数据生成
# # 需求：生成 100 行 3 列的数组
# my_array = np.random.randn(100, 3)
# print(my_array)
# # TODO 2. 数据处理和分析
# # df = pd.DataFrame(my_array)
# # # 默认有索引
# # print(df)
# df = pd.DataFrame(my_array, columns=['A', 'B','C'])
# print(df)
# print(df.describe())
#
# # TODO 3. 数据可视化
# df.plot(kind='line')
# plt.show()



# 导包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
# TODO 1. numpy 复杂数据生成
# 需求：生成 100 行 3 列的数组
my_array = np.random.randn(100, 3)
print(my_array)
# TODO 2. 数据处理和分析
df = pd.DataFrame(my_array, columns=['A', 'B', 'C'])
print(df.describe())
# df = pd.DataFrame(my_array)
# # 默认有索引
# print(df)

# TODO 3. 数据可视化
df.plot(kind='line')
plt.show()
