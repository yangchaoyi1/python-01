"""
from multiprocessing import Process
import os

def run_proc(name):
    print("子进程运行中,name=%s,pid=%d..."%(name,os.getpid()))

if __name__=='__main__':
    print('父进程 %d.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('子进程将要执行')
    p.start()
    p.join()
    print('子进程已结束')"""
from multiprocessing import Process
import time

def test():
    while True:
        print("---test---")
        time.sleep(1)

p = Process(target=test)
p.start()

while True:
    print("---main---")
    time.sleep(1)