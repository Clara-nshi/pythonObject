import time
import threading


# 1. 先定义函数
def study(a, b):
    print(f"study所在的子线程名字：{threading.current_thread().name}")
    for i in range(a, b):
        print(f'学习中...{i}')
        time.sleep(0.1)


def eat(x, y):
    print(f"eat所在的子线程名字：{threading.current_thread().name}")
    for i in range(x, y):
        print(f'吃饭中...{i}')
        time.sleep(0.1)


def sleep(a):
    print(f"sleep所在的子线程名字：{threading.current_thread().name}")
    for i in range(a, 6):
        print(f'睡觉中...{i}')
        time.sleep(0.1)


if __name__ == '__main__':
    print(f"main所在的子线程名字：{threading.current_thread().name}")
    # 2. 再调用函数
    # 创建子进程
    t1 = threading.Thread(target=study, args=(1, 6), name='study_thread')
    # 启动子进程
    t1.start()

    t2 = threading.Thread(target=eat, kwargs={'x': 1, 'y': 6}, name='eat_thread')
    t2.start()

    t3 = threading.Thread(target=sleep, args=(1, ), name='sleep_thread')
    t3.start()
