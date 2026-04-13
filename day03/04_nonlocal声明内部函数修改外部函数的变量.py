def out_func():
    num1 = 10

    def inner_func(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner_func


f = out_func()
f(1)
f(2)
f(3)
