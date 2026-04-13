# 0. 导包
# 只能获取当前进程id
import multiprocessing
# 可以获得父类进程id ppid
import os

# 1. 先定义任务
def eat():
    # print(f'eat所在主进程的编号是：{multiprocessing.current_process().pid}')
    print(f'eat所在进程编号：{os.getpid()}; 父进程编号：{os.getppid()}')
    print('吃饭中...')


def study():
    # print(f'study所在主进程的编号是：{multiprocessing.current_process().pid}')
    print(f'study所在进程编号：{os.getpid()}; 父进程编号：{os.getppid()}')
    print('学习中...')


# 2. 再调用任务
if __name__ == '__main__':
    # 先用当前的
    # print(f'main所在主进程的编号是：{multiprocessing.current_process().pid}')
    # 父进程编号是 Pycharm的进程id
    print(f'main所在进程编号：{os.getpid()}; 父进程编号：{os.getppid()}')
    eat_progress = multiprocessing.Process(target=eat)
    study_progress = multiprocessing.Process(target=study)
    eat_progress.start()
    study_progress.start()
