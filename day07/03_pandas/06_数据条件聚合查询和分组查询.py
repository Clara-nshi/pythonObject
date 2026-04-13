import pandas as pd
# todo 分组查询
read_line = pd.read_csv('emp1.txt')
print(read_line)
# 方式1 ： groupby
# 需求 ： 求各个部分的员工个数
print(read_line.groupby('dept')['name'].count())
# 需求 ： 求各个部分的平均薪资
print(read_line.groupby('dept')['sal'].mean())
# 需求 ： 求各个部分的最高薪资，最低薪资，总薪资， 平均薪资
print(read_line.groupby('dept')['sal'].agg(['max', 'min', 'sum', 'mean']))


# 方式2 ：pandas中的 pivot_table透视表
# 需求 ： 求各个部分的员工个数
print(read_line.pivot_table(index='dept', values='name', aggfunc='count'))
# 需求 ： 求各个部分的平均薪资
print(read_line.pivot_table(index='dept', values='sal', aggfunc='mean'))
# 需求 ： 求各个部分的最高薪资，最低薪资，总薪资
print(read_line.pivot_table(index='dept', values='sal', aggfunc=['max', 'min', 'sum', 'mean']))


