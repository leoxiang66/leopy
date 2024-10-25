import leopy.leoroutine as lrt
import time

# 使用示例
def some_job(x, y,t):
    time.sleep(t)
    return x + y

def on_job_done(result):
    print(f"Job done with result: {result}")

if __name__ == "__main__":
    manager = lrt.ThreadManager()
    manager.start_new_job(some_job,x=1,y= 2, t=9,callback=on_job_done)
    time.sleep(1)
    manager.start_new_job(some_job,x=1,y= 3, t=3,callback=on_job_done)
    time.sleep(1)
    manager.start_new_job(some_job,x=1,y= 4,t=2, callback=on_job_done)
    time.sleep(3)
    manager.wait_all_jobs()