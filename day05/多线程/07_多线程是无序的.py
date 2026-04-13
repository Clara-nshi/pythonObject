# 1. 导包
import threading
import time


# 定义任务
def show():
    # 线程做同一个任务，最后结果是无序的
    time.sleep(1)     # 模拟程序运行时间
    print(f'{threading.current_thread().name}')


if __name__ == '__main__':
    # 2. 创建对象
    for i in range(1, 6):
        t = threading.Thread(target=show)
        t.start()



#
# # 1. 导包
# import multiprocessing
# import time
#
#
# # 定义任务
# def show():
#     # 线程做同一个任务，最后结果是无序的
#     time.sleep(1)    # 模拟程序运行时间
#     print(f'{multiprocessing.current_process().name}')
#
#
# if __name__ == '__main__':
#     # 2. 创建对象
#     for i in range(1, 6):
#         t = multiprocessing.Process(target=show)
#         t.start()
#
