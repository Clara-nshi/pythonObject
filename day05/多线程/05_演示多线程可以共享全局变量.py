# 1， 定义全局变量
import threading
import time
import os

my_list = []


# 定义任务1 ：写入1， 2， 3
def write_data():
    print(f'write_data所在进程ID：{os.getpid()}')
    for i in range(1, 4):
        my_list.append(i)
    print(f'write_data线程中访问已经修改的全局变量：{my_list}')


# 定义任务2 ： 直接读取全局变量
def read_data():
    print(f'read_data所在进程ID：{os.getpid()}')
    print(f'read_data线程中访问已经修改的全局变量：{my_list}')


# 调用多任务
if __name__ == '__main__':
    print(f'main所在进程ID：{os.getpid()}')
    print(f'main所在的进程id：')
    # 创建多线程
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)
    # 启动线程
    t1.start()
    time.sleep(1)
    t2.start()

