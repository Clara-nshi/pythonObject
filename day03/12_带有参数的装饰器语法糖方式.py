# 3. 定义装饰器要求打印正在做加法运算
def deco(flag):
    def out_func(fn):
        def inner_func(x, y):
            if flag == '+':
                print('正在做加法运算...')
            elif flag == '-':
                print('正在做减法运算')
            result = fn(x, y)
            return result
        return inner_func
    return out_func


# 4. 添加装饰器
@deco("+")
# 1. 先定义函数
def add(a, b):
    result = a + b
    return result


@deco("-")
def diff(a, b):
    result = a - b
    return result


# 2. 再调用函数
print(add(1, 4))
print(diff(2, 4))

