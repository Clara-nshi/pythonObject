# 1. 导包
import threading

# 2. 定义全局变量
g_num = 0


# 3. 往全局变量上加100w次1
def sum1(lock):
    global g_num
    # TODO 上锁
    lock.acquire()
    for i in range(1000000):
        g_num += 1
    # TODO 释放锁
    lock.release()
    print(f'任务11111111：{g_num}')


# 4. 往全局变量上加100w次1
def sum2(lock):
    global g_num
    # TODO 上锁
    lock.acquire()
    for i in range(1000000):
        g_num += 1
    # TODO 释放锁
    lock.release()
    print(f'任务22222222：{g_num}')


if __name__ == '__main__':
    # 创建进程互斥锁
    lock = threading.Lock()
    # 传参，保证多任务用的是同一个锁
    t1 = threading.Thread(target=sum1, args=(lock, ))
    t2 = threading.Thread(target=sum2, args=(lock, ))
    # 开启多线程
    t1.start()
    t2.start()


