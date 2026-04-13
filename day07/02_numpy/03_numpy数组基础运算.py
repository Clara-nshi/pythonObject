import numpy as np
# 创建任意两个数组，形状一致
a1 = np.array([1, 2, 3, 4])
a2 = np.array([2, 3, 4, 5])
a3 = np.array([5])
print('==============')
print(a1 + a2)
print(np.add(a1, a2))

print(a1 - a2)
print(np.subtract(a1, a2))

print(a1 * a2)
print(np.multiply(a1, a2))

print(a1 / a2)
print(np.divide(a1, a2))

print(a1 // a2)
print(a1 ** a2)
print(a1 % a2)

print('==========')


# 演示基础运算(返回True和False)
print(a1 > a2)
print(a1 > a3)
print(a1 > 2)
print(a1 == 2)
print(a1 == a2)





