# """
# iloc(): 根据索引查找  格式 -> df.iloc[行索引, 列索引]   左闭右开
# loc(): 根据标签查找   格式 -> df.loc[行标签, 列标签]   左闭右闭
# 注意：当没有额外设置标签的时候，此时标签就是索引
# """
# import pandas as pd
# read_file = pd.read_csv('students.txt', sep=',', names=['name', 'age', 'sex', 'score'])
# print(read_file)
# # 需求：获取第 1 行数据
# # Series对象
# # 由于没有设置行标签，此时行标签就是索引
# print(read_file.iloc[0])
# print(read_file.loc[0])
# # 需求：获取前 3 行数据
# print("***********************")
# print(read_file.iloc[0: 3])
# print(read_file.loc[0:2, :])
# print(read_file.loc[0:2])
# # 需求：获取 1， 3 行数据
# print('========================')
# print(read_file.iloc[[0, 2], :])
# print(read_file.loc[[0, 2], :])
# print('========================')
#
#
#
#
# # 需求：获取第 1 列数据
# print(read_file.iloc[:, 0])
# print(read_file.loc[:, 'name'])
#
# # 需求：获取第 1, 3 列数据
# print(read_file.iloc[:, [0, 2]])
# print(read_file.loc[:, ['name', 'sex']])
#
# # 需求：获取前 3 列数据
# print(read_file.iloc[:, 0:3])
# print(read_file.loc[:, 'name':'sex'])




"""
iloc(): 根据索引查找  格式 -> df.iloc[行索引, 列索引]   左闭右开
loc(): 根据标签查找   格式 -> df.loc[行标签, 列标签]   左闭右闭
注意：当没有额外设置标签的时候，此时标签就是索引
"""
import pandas as pd
read_file = pd.read_csv('students.txt', sep=',', names=['name', 'age', 'sex', 'score'])
print(read_file)
# 需求：获取第 2 行数据
print('第2行数据', read_file.iloc[1])
print('第2行数据', read_file.loc[1])
# Series对象
# 由于没有设置行标签，此时行标签就是索引
# 需求：获取前 3 行数据
print('前3行数据', read_file.iloc[0:3, :])
print('前3行数据', read_file.loc[0:2, :])
print("***********************")
# 需求：获取 1， 3 行数据
print('========================')
print('========================')




# 需求：获取第 1 列数据

# 需求：获取第 1, 3 列数据

# 需求：获取前 3 列数据

