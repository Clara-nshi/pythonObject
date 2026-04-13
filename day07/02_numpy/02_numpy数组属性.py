# 1. 导包
import numpy as np
# 2. 创建任意一维数组
my_array = np.arange(12)
print(my_array)
# 3. reshape 一维变二维
reshape_array = my_array.reshape(3, 4)
print(reshape_array)
print(reshape_array.ndim, reshape_array.size, reshape_array.dtype)
# 4. 使用数组.T做转置
t_resize_array = reshape_array.T
print(t_resize_array)
# 5. 使用展平操作(n维转换为1维)
fla_array = t_resize_array.flatten()
print(fla_array)
# 6. 使用resize
"""
上面生成了12个数据，（2， 8）需要16个数据
改变形状，不够就补
参考原有数组的内容，修改成新的形状
[[ 0  1  2  3  4  5  6  7]
 [ 8  9 10 11  0  1  2  3]]
 """
resize_array = np.resize(fla_array, (2, 8))
print(resize_array)