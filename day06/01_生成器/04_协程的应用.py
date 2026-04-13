# 导包
import asyncio


# 1. 定义协程函数
# TODO 调用协程函数，返回的是协程对象
async def get_name(name):
    print(f'{name}开始')
    await asyncio.sleep(1)
    print(f'{name}结束')

# 调用函数
# 同步调用任务：一个个执行
asyncio.run(get_name('张三'))
asyncio.run(get_name('李四'))
print('=================')


# 异步调用：借助一个额外的函数
async def app():
    # 并发调用任务
    task1 = asyncio.create_task(get_name('张三'))
    task2 = asyncio.create_task(get_name('李四'))
    # 调用太快，只出现开始，没有结束，使用await等待程序运行完
    await task1
    await task2

# 运行协程函数
asyncio.run(app())

