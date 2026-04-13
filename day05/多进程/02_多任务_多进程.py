# import time
# import multiprocessing
#
#
# # 1. 先定义函数
# def study():
#     for i in range(1, 6):
#         print(f'学习中...{i}')
#         time.sleep(0.1)
#
#
# def eat():
#     for i in range(1, 6):
#         print(f'吃饭中...{i}')
#         time.sleep(0.1)
#
#
# def sleep():
#     for i in range(1, 6):
#         print(f'睡觉中...{i}')
#         time.sleep(0.1)
#
#
# def game():
#     for i in range(1, 6):
#         print(f'游戏中...{i}')
#         time.sleep(0.1)
#
#
# # 2. 再调用函数
# # TODO: 多进程必须添加 main判断，否则报错
# if __name__ == '__main__':
#     # 创建子进程
#     p1 = multiprocessing.Process(target=study)
#     # 启动子进程
#     p1.start()
#
#     p2 = multiprocessing.Process(target=eat)
#     p2.start()
#
#     p3 = multiprocessing.Process(target=sleep)
#     p3.start()
#
#     p4 = multiprocessing.Process(target=game)
#     p4.start()


import time
import multiprocessing


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
# TODO: 多进程必须添加 main判断，否则报错
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=study)
    p2 = multiprocessing.Process(target=eat)
    p3 = multiprocessing.Process(target=sleep)
    p4 = multiprocessing.Process(target=game)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
