# # 3. 需求：定义两个装饰器，分别是登录功能和验证码功能
# def out_func_login(f):
#     def inner_func():
#         # 额外功能
#         print('登录功能...')
#         f()     # TODO 此处就是原有函数
#     return inner_func
#
#
# def out_func_code(f):
#     def inner_func():
#         # 额外功能
#         print('验证码功能...')
#         f()     # TODO 此处就是原有函数
#     return inner_func
#
# # 4. 使用语法糖方式装饰器
# @out_func_code
# @out_func_login
# # 1. 先定义函数
# def content():
#     print('开始发表评论...此处省略1k行代码')
#
#
# # 2. 再调用函数
# content()


# # 3. 需求：定义两个装饰器，分别是登录功能和验证码功能
# def out_func_login(f):
#     def inner_func():
#         # 额外功能
#         print('登录功能...')
#         f()     # TODO 此处就是原有函数
#     return inner_func
#
#
# def out_func_code(f):
#     def inner_func():
#         # 额外功能
#         print('验证码功能...')
#         f()     # TODO 此处就是原有函数
#     return inner_func
#
#
# # 1. 先定义函数
# def content():
#     print('开始发表评论...此处省略1k行代码')
#
#
#
#
# # 4.使用语法糖方式装饰器
# content = out_func_login(content)
# content = out_func_code(content)
# content()

# # 3. 需求：定义两个装饰器，分别是登录功能和验证码功能
def out_func_login(fn):
    def inner():
        print("登录功能...")
        fn()

    return inner


def out_func_code(fn):
    def inner():
        print("验证功能...")
        fn()

    return inner


def content():
    print("评论功能...")


content = out_func_code(content)
content = out_func_login(content)
content()
