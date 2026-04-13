# 1. 有嵌套
def out_func(num1):
    num1 = 10
    
    def inner_func(num2):
        # 2. 有引用
        print(num1 + num2)
    # 3. 有返回
    return inner_func    # TODO 返回的是地址


f = out_func()   # TODO 此处本质是 f = inner_func
print(f)   # TODO 此处 f 就代表内部函数: <function out_func.<locals>.inner_func at 0x0000021569918860>
f(2)
f(1)
f(3)
