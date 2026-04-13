# 1. 先定义函数
def show(n):
    for i in range(n):
        return i         # 直接结束


def generator_func(n):
    for i in range(n):
        yield i


# 2. 再调用函数
print(show(5))      # 0
print(show(5))      # 还是0


# 3. 调用generator_func
my_generator = generator_func(6)
print(my_generator, type(my_generator))
# 4. next() -> 一次拿一个
print(next(my_generator))       # 0
print(next(my_generator))       # 1（next相当于暂停）
# 5. for 循环遍历，拿剩下的所有
for i in my_generator:
    print(i)                # 2 3 4 5 
