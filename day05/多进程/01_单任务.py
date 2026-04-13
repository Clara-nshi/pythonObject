# 1. 先定义函数
import time


def study():
    time.sleep(2)
    print('学习中...')


def eat():
    time.sleep(2)
    print('吃饭中...')


def sleep():
    time.sleep(2)
    print('睡觉中...')


def game():
    time.sleep(2)
    print('游戏中...')


# 2. 再调用函数
# 理论上应该有一个main判断，此处省略
study()
eat()
sleep()
game()
