import leopy.leoroutine as lrt

# 使用示例
def some_job(x, y):
    return x + y

def on_job_done(result):
    print(f"Job done with result: {result}")

if __name__ == "__main__":
    manager = lrt.ThreadManager()
    manager.start_new_job(some_job,x=1,y= 2, callback=on_job_done)
    manager.wait_all_jobs()