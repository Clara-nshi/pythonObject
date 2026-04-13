# 1. 先定义函数
def show():
    # print('hello')
    a = 'hello'
    # 默认此处补充 return None
    # 如果没有 return返回值，默认最后一行补充 return None
    return a


# 2. 再调用函数
print(show())
# 单单函数名找内存地址
print(show)     # <function show at 0x00000273CDDB05E0>
print('=============================')
f = show        # TODO 函数名默认传递的是它传递的函数地址
print(f)        # <function show at 0x00000273CDDB05E0>
print(f())
print('===========================')


def do(func):
    print(func())
    print(func)     # <function show at 0x00000273CDDB05E0>


do(show)
# name 'a' is not defined
# print(a)   # 局部变量是伴随着函数的调用而创建，然后伴随着函数的结束而销毁
# 全局变量是伴随着当前主程序的调用而创建，然后伴随着主程序的结束而销毁
