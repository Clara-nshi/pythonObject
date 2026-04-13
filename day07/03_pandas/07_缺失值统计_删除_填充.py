# 导包
import pandas as pd
# 读取文件
df = pd.read_csv('清洗数据.csv')
print(df)
# 查看各个列非空数量
df.info()
# 查看各个列缺失值数量
print(df.isnull().sum())
# 缺失值占比
print(df.isnull().sum()/len(df))

print('******************************')
# 删除缺失值占比高的列
print(df.drop('B', axis=1))
print(df.dropna(how='any'))
print(df.dropna(how='all'))
print('*********************************8')
# 把 A 所在的缺失的行都删掉
print(df.dropna(subset=['A']))
print('*********************************8')

"""
print(df.drop('B', axis=1))
B真删了
"""
# df.drop('B', axis=1, inplace=True)
# print(df)
# 填充缺失值
print(df.fillna(value=df.mean()))
# 填充跟上方值一样的
print(df.ffill())
# 填充跟下方值一样的
print(df.bfill())


