import time


def out_func(f):
    # 有嵌套
    def inner_func(*args, **kwargs):
        # 有额外功能
        print(f'正在做求和计算...')
        # 有引用
        sum = f(*args, **kwargs)  # TODO 此处就是在调用原有函数
        return sum

    # 有返回
    return inner_func

@out_func
# 1. 先定义原有函数（功能是求任意个数字的和）
def get_sum(*args, **kwargs):
    time.sleep(5)
    sum = 0
    for i in args:
        sum += i

    for v in kwargs.values():
        sum += v
    return sum


# 2. 再调用函数
sum = get_sum(1, 2, 3, a=4, b=5, c=6)
print(f'最终计算结果为：{sum}')
