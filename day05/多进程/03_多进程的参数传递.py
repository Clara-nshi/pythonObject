"""
多进程中的参数传递
方式1 -> arg : 以元组形式传参
方式2 -> kwargs : 以字典形式传参
"""
import time
import multiprocessing


# 1. 先定义函数
def study(a, b):
    print(f'study所在的当前进程的名字是：{multiprocessing.current_process().name}')
    for i in range(a, b):
        print(f'学习中...{i}')
        time.sleep(0.1)


def eat(x, y):
    print(f'eat所在的当前进程的名字是：{multiprocessing.current_process().name}')
    for i in range(x, y):
        print(f'吃饭中...{i}')
        time.sleep(0.1)


def game(a):
    print(f'game所在的当前进程的名字是：{multiprocessing.current_process().name}')
    for i in range(a, 6):
        print(f'游戏中...{i}')
        time.sleep(0.1)


# 2. 再调用函数
# TODO: 多进程必须添加 main判断，否则报错
if __name__ == '__main__':
    print(f'main所在的当前进程的名字是：{multiprocessing.current_process().name}')
    # 创建子进程
    # 字典通过关键字传参，不推荐
    study_process = multiprocessing.Process(target=study, kwargs={'a': 1, 'b': 5})
    # 启动子进程
    study_process.start()
    study_process.join()    # 主进程等待这个子进程结束

    eat_process = multiprocessing.Process(target=eat, args=(1, 5))
    eat_process.start()

    # TODO 用元组传单个参数需要加逗号
    game_process = multiprocessing.Process(target=game, args=(1,))
    game_process.start()


