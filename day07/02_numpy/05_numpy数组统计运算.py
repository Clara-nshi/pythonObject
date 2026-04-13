# 导包
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

# sum() 求和
print(arr.sum())
print(np.sum(arr))
# 按照列求和（axis不一样的包里，代表的行列不一定）
print(np.sum(arr, axis=0))
# 按照行求和
print(np.sum(arr, axis=1))

# mean()求平均数
print(arr.mean())
print(np.mean(arr))
print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))


# max求最大值
print(arr.max())
print(np.max(arr))
print(np.max(arr, axis=0))
print(np.max(arr, axis=1))


# min求最小值
print(arr.min())
print(np.min(arr))
print(np.min(arr, axis=0))
print(np.min(arr, axis=1))


# 求方差
print(arr.var())
print(np.var(arr))
print(np.var(arr, axis=0))
print(np.var(arr, axis=1))

# 求标准差
print(arr.std())
print(np.std(arr))
print(np.std(arr, axis=0))
print(np.std(arr, axis=1))


# argmax() 索引最大值
print(arr.argmax())
print(np.argmax(arr))
print(np.argmax(arr, axis=0))
print(np.argmax(arr, axis=1))
# argmin() 索引最小值
print(arr.argmin())
print(np.argmin(arr))
print(np.argmin(arr, axis=0))
print(np.argmin(arr, axis=1))
# argwhere() 索引所有满足条件的值
print(np.argwhere(arr > 5))
print(np.argwhere(arr < 5))
print(np.argwhere(arr == 5))
print(np.argwhere(arr != 5))
print(np.argwhere(arr >= 5))
print(np.argwhere(arr <= 5))
print(np.argwhere(arr % 2 == 0))
print(np.argwhere(arr % 2 != 0))
print(np.argwhere(arr % 2 > 0))
print(np.argwhere(arr % 2 < 0))
print(np.argwhere(arr % 2 >= 0))
print(np.argwhere(arr % 2 <= 0))
print(np.argwhere(arr % 2 > 1))
print(np.argwhere(arr % 2 < 1))
