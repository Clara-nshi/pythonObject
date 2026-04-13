"""
矩阵乘法：矩阵乘法要求第一个矩阵的列数必须等于第二个矩阵的行数
矩阵乘法常用符号和api: @ np.matmul()
公式：(m, n) @ (n, z) 最后结果形状(m, z)
注意：np.dot()是特殊的

    np.dot：支持一维向量点积，对二维以上数组行为不统一
    np.matmul：专门做矩阵乘法，一维向量不支持，高维按 batch 处理更规范

一句话：一维用 dot，二维及以上推荐 matmul/@，高维数组 matmul 更安全。
"""
import numpy as np

# 定义两个 2x2 矩阵
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# 1. 推荐写法：@ 符号
C1 = A @ B

# 2. matmul（矩阵乘法专用）
C2 = np.matmul(A, B)

# 3. dot（二维矩阵等价于矩阵乘法）
# 不推荐
C3 = np.dot(A, B)

# 检查是否一致
print(C1 == C2)

print(C1)
print(C2)
print(C3)



