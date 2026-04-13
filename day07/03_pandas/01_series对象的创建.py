# 导包
import pandas as pd

# pandas 中的一维结构：Series
# 创建 s 对象
# 方式1： 通过列表创建
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='score')
print(s, type(s))
# 行索引 a,b,c,d,e, name 为列索引
# s 对象的值本质就是ndarray
print(s.values, type(s.values))
# [1 2 3 4 5] <class 'numpy.ndarray'>
# 方式2： 通过字典创建
s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, name='score')
print(s, type(s))
# 原本的索引还在，只不过又给他起了一个索引
# 获取s对象的属性
print(s.ndim, s.shape, s.dtype, s.size)
