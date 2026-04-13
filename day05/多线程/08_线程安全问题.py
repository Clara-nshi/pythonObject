import threading
# 1. 定义全局变量
g_num = 0


# 任务1 ： 加100万次1
def count_sum1():
    global g_num
    for i in range(1, 1000001):
        g_num += 1
    print(f'总和1：{g_num}')


# 任务2 ： 加100万次1
def count_sum2():
    global g_num
    for i in range(1, 1000001):
        g_num += 1
    print(f'总和2：{g_num}')


if __name__ == '__main__':
    # 创建多线程
    # 使用低版本效果明显
    t1 = threading.Thread(target=count_sum1)
    t2 = threading.Thread(target=count_sum2)
    t1.start()
    t2.start()

