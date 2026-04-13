import 时间装饰器


# 1. 先定义原有函数，功能是计算1-1000000

@时间装饰器.out_func
def get_sum(a, b):
    sum = 0
    for i in range(a, b + 1):
        sum += i
    print(sum)


# 2. 再调用函数
get_sum(1, )
