# 2--class base thread
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(1,11):
            time.sleep(1)   # execute hone me (1) second ka time lega
            print("This is Child Thread....!")
t1=MyThread()
t1.start()
for i in range(1,11):
    time.sleep(0.5)     # execute hone me (0.5) second ka time lega
    print("this is Main Thread.!!")

#output 
# this is Main Thread.!!
# This is Child Thread....!
# this is Main Thread.!!
# this is Main Thread.!!
# This is Child Thread....!
# this is Main Thread.!!
# this is Main Thread.!!
# This is Child Thread....!
# this is Main Thread.!!
# this is Main Thread.!!
# This is Child Thread....!
# this is Main Thread.!!
# this is Main Thread.!!
# This is Child Thread....!
# this is Main Thread.!!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!