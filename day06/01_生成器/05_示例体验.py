import asyncio
import time
import threading


# 模拟网络请求
def mock_io(delay, name):
    time.sleep(delay)
    return f"{name}完成"


# 1. 普通顺序执行（慢）
def sync_version():
    start = time.time()
    mock_io(1, "任务1")
    mock_io(1, "任务2")
    print(f"同步: {time.time()-start:.1f}秒")


# 2. 多线程执行（快一点）
def thread_version():
    start = time.time()
    t1 = threading.Thread(target=mock_io, args=(1, "线程1"))
    t2 = threading.Thread(target=mock_io, args=(1, "线程2"))
    t1.start()
    t2.start()
    t1.join()     # 保证两个任务都执行外
    t2.join()
    print(f"线程: {time.time()-start:.1f}秒")


# 3. 协程执行（最快）
async def async_version():
    start = time.time()

    async def async_io(delay, name):
        await asyncio.sleep(delay)
        return f"{name}完成"

    # 并发执行
    task1 = asyncio.create_task(async_io(1, "协程1"))
    task2 = asyncio.create_task(async_io(1, "协程2"))
    await task1
    await task2

    print(f"协程: {time.time()-start:.1f}秒")

# 运行对比
print("=== 执行时间对比 ===")
sync_version()  # 约2秒
thread_version()  # 约1秒
asyncio.run(async_version())   # 约1秒