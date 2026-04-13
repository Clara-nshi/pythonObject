# 导包
import pandas as pd
# 准备数据
df = pd.read_csv('emp.txt')
print(df)
# todo 1. 数据基础查询
# 查询所有员工的姓名和薪资
print(df[['name', 'sal']])
# todo 2. 条件查询
# 获取薪资大于5000的员工信息
print(df[df['sal'] > 5000])
# 获取技术部员工的信息
# print(df[df['dept'] == '"技术部"'])
# 方案2：精准匹配（带空格+带引号）
print(df[df['dept'] == ' "技术部"'])

# 是技术部且薪资大于5000
print(df[(df['dept'] == ' "技术部"') & (df['sal'] > 5000) ])
print("***********************")
print(df.query('sal > 5000 and dept == \' "技术部"\''))


# todo 3. 排序查询
# 需求：薪资从高到低
print(df.sort_values('sal', ascending=False))
# 需求：薪资从低到高
print(df.sort_values('sal', ascending=True))

print('***********************')
# todo 4. 聚合函数
print('************************获取每个列的值**************************************')
print(df.count())
# 需求：获取员工数量
print(len(df))
print(df.shape[0])
print(len(df.index.value_counts()))

# 需求：获取最高薪资
print(df['sal'].max())
# 需求：获取最高薪资的所有信息
print(df[df['sal']==df['sal'].max()])
# 需求：获取平均薪资和总薪资包
print(df['sal'].sum())

