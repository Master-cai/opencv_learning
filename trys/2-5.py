import threading, time


def doWaiting():
    print('start waiting :', time.strftime('%s'))
    time.sleep(3)
    print('stop waiting', time.strftime('%s'))
    thread1 = threading.Thread(target=doWaiting())
    thread1.start()
    time.sleep(1)
    print('start join')
    thread1.join()
    print('end join')

doWaiting()