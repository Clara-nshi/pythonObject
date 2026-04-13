# 导包
import numpy as np
# 1. 把列表转换为数组
my_array = np.array([1, 2, 3, 4, 5])
print('一维数组：', my_array, my_array.ndim, my_array.shape, my_array.size)
# 列前后要对应上
my_array = np.array([[1, 2], [3, 4]])
print('二维数组', my_array, my_array.ndim, my_array.shape)

# 2. 创建全0全1的数组
zero_array=np.zeros(5)
print(zero_array, zero_array.ndim, zero_array.shape)
zero_array=np.zeros(5,)
print(zero_array, zero_array.ndim, zero_array.shape)
zero_ndarray=np.zeros((3, 4))
print(zero_ndarray, zero_ndarray.ndim, zero_ndarray.shape)
one_ndarray = np.ones((2, 3))
print(one_ndarray, one_ndarray.ndim, one_ndarray.shape)

# 3. 按照范围和等差方式创建
# 直接指定步长
arange_array = np.arange(1, 10)
print(arange_array, arange_array.ndim, arange_array.shape)

arange_array = np.arange( 10)
print(arange_array, arange_array.ndim, arange_array.shape)

# 等差[ 1.    3.25  5.5   7.75 10.  ] 1 (5,)
linspace_array = np.linspace(start=1, stop=10, num=5)
print(linspace_array, linspace_array.ndim, linspace_array.shape)

# 4. 随机生成数组
# 0~1
randint_array = np.random.rand(2, 3)
print(randint_array, randint_array.ndim, randint_array.shape)
# 正态分布
normal_array = np.random.randn(2, 4)
print(normal_array, normal_array.ndim, normal_array.shape)
# 开始-结束0形状
shape_array = np.random.randint(1, 10, size=(2, 3))
print(shape_array, shape_array.ndim, shape_array.shape)







