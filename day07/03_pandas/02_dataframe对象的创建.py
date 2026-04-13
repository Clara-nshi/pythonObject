# 导包
import pandas as pd

# pandas 中的二维结构：dataframe
# 创建 df 对象
# 方式1： 通过列表创建
df = pd.DataFrame([['clara', 20, '女'], ['mike', 23, '女']], index=['a', 'b'], columns=['name', 'age', 'sex'])
print(df, type(df))
# df 对象的 value值本质就是ndarray二维数组
print(df.values, type(df.values))
# 方式2： 通过字典创建 字典的 key 就是列标签
print('22222222222222')
df = pd.DataFrame({'name': ['clara', 'mike'], 'age': [18, 23], 'sex': ['男', '女']}, index=['a', 'b'])
print(df, type(df))
# 获取 s 对象的属性
print(df.ndim, df.shape, df.size)
print(df.dtypes)
# 
