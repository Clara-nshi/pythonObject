import time
import threading


# 1. 先定义任务
def study():
    for i in range(20):
        print(f'{threading.current_thread().name}子进程任务执行中...{i}')
        time.sleep(0.1)
    print(f'{threading.current_thread().name}主进程任务结束...')


# 2. 再调用任务
if __name__ == '__main__':
    print(f'{threading.current_thread().name}主进程任务执行中...')
    # 创建子进程
    study_process = threading.Thread(target=study)
    # TODO（推荐） 在开启子进程之前，设置守护主进程
    # study_process = multiprocessing.Process(target=study, daemon=True)
    study_process.daemon = True
    # 开启子进程
    study_process.start()
    # 模拟主进程用了0.5秒
    time.sleep(1)
    print(f'{threading.current_thread().name}主进程任务结束...')
    # TODO 方式2：在开启子进程之后，强制终止它(不推荐)， 僵尸进程，不会清理资源


