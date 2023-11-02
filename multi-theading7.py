# 2--class base thread
import threading
import time

#  test()  function ko call karenge to pahle ---(test thread only 1 time) -- call hoga useke bad --- main thread bar bar call hogi

class MyThread(threading.Thread):
    def run(self):
        for i in range(1,11):
            time.sleep(1)
            print("This is Child Thread....!")
    def test (self):
        print(" This is a Test thread ")
t1=MyThread()
# t1.start()
# t1.join()
t1.test()
# t1.run()            # normal function ki tarah hi call hoga - pahle child thread - phir main thread hoga
for i in range(1,11):
    time.sleep(0.5)
    print("this is Main Thread.!!")



#     This is a Test thread 
# this is Main Thread.!!
# this is Main Thread.!!
# this is Main Thread.!!
# this is Main Thread.!!
# this is Main Thread.!!
# this is Main Thread.!!
# this is Main Thread.!!
# this is Main Thread.!!
# this is Main Thread.!!
# this is Main Thread.!!