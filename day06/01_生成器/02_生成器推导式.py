"""
生成器：不提前准备好
返回一个对象
没有生成，提前记录好
"""
# TODO 一  如何使用生成器推导式
my_generator = (i for i in range(5))
print(my_generator, type(my_generator))
# TODO next调用(调用几次，生成几次)
print(next(my_generator))
print(next(my_generator))
# TODO for 遍历所有，一次拿剩下的所有，上面已经拿了两个，还剩三个
for i in my_generator:
    print(i)
