import multiprocessing
import os
import time

# 定义全局变量
my_list = []
a = 10


# 定义任务1： 往全局变量中添加1， 2， 3三个元素
def write_data():
    print(f'write进程id: {os.getpid()}')
    for i in range(1, 4):
        my_list.append(i)
    print(f'write中访问全局变量：{my_list}')


# 定义任务2： 直接读取全局变量
def read_data():
    print(f'read进程id: {os.getpid()}')
    print(f'read中访问全局变量：{my_list}')


if __name__ == '__main__':
    print(f'main进程id: {os.getpid()}')
    write_data()
    read_data()

