import time


# 3. 定义装饰器：计算任意函数的执行时间
def out_func(f):
    def inner_func(x, y):
        start = time.time()
        f(x, y)
        end = time.time()
        print(f'此计算执行的{end - start}s')

    return inner_func



