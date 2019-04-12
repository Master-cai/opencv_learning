import threading
import time
import random

count = 0
class MyThread(threading.Thread):
    def __init__(self, lock, threadName):
        super(MyThread, self).__init__(name=threadName)
        self.lock = lock

    def run(self):
        global count
        self.lock.acquire()#将当前线程锁定 使其他线程无法访问全局变量count
        for i in range(100):
            count = count + 1
            time.sleep(0.3)
            print(self.getName(), count)
        self.lock.release()#线程执行完毕 释放该线程 使其他线程可以继续操作


Lock = threading.Lock()
for i in range(50):
    MyThread(Lock, "MythreadName:" + str(i)).start()
