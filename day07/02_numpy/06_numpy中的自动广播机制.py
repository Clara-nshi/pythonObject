# 导包
import numpy as np
# 设置种子：保证每次生成的数据相同(my_array = np.random.randint生成的数固定)
np.random.seed(666)
# 准备一个 3 行 3 列的数组
my_array = np.random.randint(10, size=(3, 3))
print(my_array)
# TODO 2. numpy 数组的广播机制
# 准备 1 行 3 列数据
a1 = np.array([[1, 2, 3]])
# 准备 3 行 1 列数据
a2 = np.array([[1], [2], [3]])
# 演示自动广播
print(my_array + a1)
print(my_array + a2)
