import time
import threading


# 1. 先定义函数
def study():
    for i in range(1, 6):
        print(f'学习中...{i}')
        time.sleep(0.1)


def eat():
    for i in range(1, 6):
        print(f'吃饭中...{i}')
        time.sleep(0.1)


def sleep():
    for i in range(1, 6):
        print(f'睡觉中...{i}')
        time.sleep(0.1)


def game():
    for i in range(1, 6):
        print(f'游戏中...{i}')
        time.sleep(0.1)


# 2. 再调用函数
# 创建子进程
t1 = threading.Thread(target=study)
# 启动子进程
t1.start()

t2 = threading.Thread(target=eat)
t2.start()

t3 = threading.Thread(target=sleep)
t3.start()

t4 = threading.Thread(target=game)
t4.start()
