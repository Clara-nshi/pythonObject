# 导包
import numpy
import pandas as pd
# 读取文件生成 df 对象
# csv：以固定符号分隔的文本文件，默认分隔符为","逗号
df_read = pd.read_csv('students.txt', names=['name', 'age', 'sex', 'score'])
print(df_read)
print(type(df_read))
print(df_read.values)
print(df_read.ndim, df_read.shape, df_read.size)
print('============')
print(df_read.columns)
print(df_read.index)
print(df_read.values)
print(df_read.dtypes)
# 查看数据
print('===========')
# 取最前面两个
print(df_read.head(2))
# 取最后面两个
print(df_read.tail(2))
# 描述性统计
print(df_read.describe())
print('============')
# 获取各个列是否为空
df_read.info()
print('=============')
# 根据类名获取对应列数据
print(numpy.nan)
# Name: name, dtype: str <class 'pandas.Series'>
print(df_read['name'], type(df_read['name']))
# 6  NaN    NaN <class 'pandas.DataFrame'>
print(df_read[['name', 'score']], type(df_read[['name', 'score']]))
# 需求：获取 score>98的数据
b = df_read['score'] > 98       # 此处 b 本质是一个布尔数组
print(df_read[b])               # 自动把 True 所在行取出
print('===============')
c = df_read['sex'].str.contains('男')
print(df_read[c])
