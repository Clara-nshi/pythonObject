# 3. 定义装饰器要求打印正在做加法运算

def out_func_add(fn):
    def inner_func(x, y):
        print('正在做加法运算...')
        fn(x, y)

    return inner_func


def out_func_diff(fn):
    def inner_func(x, y):
        print('正在做减法运算...')
        fn(x, y)

    return inner_func


# 4. 添加装饰器
# 1. 先定义函数
def add(a, b):
    print(a + b)


def diff(a, b):
    print(a - b)


# 2. 再调用函数
add = out_func_add(add)
add(1, 4)
diff = out_func_diff(diff)
diff(5, 3)
