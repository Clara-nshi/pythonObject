"""
不改变原有函数
装饰器：不改变原有函数的基础上，添加额外的功能
"""


def check(fn):     # f = comment
    def inner():
        print('请先登录...自动跳转登录功能...')
        fn()
    return inner


# 1. 先定义原有函数
@check
def comment():
    # 0. 提前定义登录功能函数
    # print('请先登录...自动跳转登录功能...')
    print('发表评论功能...此处省略1k行代码....')


# # 2. 调用原有函数之前：使用原有装饰器方式修饰函数
# comment = check(comment)
# 此处调用的本质是check返回的内部函数inner
comment()
print(comment.__name__)


