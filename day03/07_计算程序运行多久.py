import time


# 3. 定义装饰器：计算任意函数的执行时间
def out_func(f):
    def inner_func(x, y):
        start = time.time()
        f(x, y)
        end = time.time()
        print(f'此计算执行的{end - start}s')

    return inner_func


# 1. 先定义原有函数，功能是计算1-1000000
@out_func
def get_sum(a, b):
    sum = 0
    for i in range(a, b + 1):
        sum += i
    print(sum)


# 2. 再调用函数
get_sum(1, 1000000001)
