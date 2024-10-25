import leopy.leoroutine as lrt
import asyncio

async def some_coroutine(x, y,t):
    print(f'sleep {t}s')
    await asyncio.sleep(t)  # 模拟 I/O 操作
    return x + y

def on_job_done(result):
    print(f"Job done with result: {result}")

async def main():
    manager = lrt.CoroutineManager()
    manager.start_new_job(some_coroutine,x= 1,y= 2,t=3, callback=on_job_done)
    manager.start_new_job(some_coroutine,x= 2,y= 2,t=5, callback=on_job_done)
    manager.start_new_job(some_coroutine,x= 3,y= 2,t=1, callback=on_job_done)
    
    await asyncio.sleep(3)
    await manager.wait_all_jobs()

# 运行主函数
if __name__ == "__main__":
    asyncio.run(main())