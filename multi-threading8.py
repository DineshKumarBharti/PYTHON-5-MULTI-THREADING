# 2--class base thread
import threading
import time

#  super().start()  
#  parent 

class MyThread(threading.Thread):
    def run(self):
        for i in range(1,11):
            time.sleep(1)
            print("This is Child Thread....!")
    def test (self):
        super().start()   # parent thread ko call karega -- to parent  (test thread-1time)--(child thread--&-main thread---again and again chalta rahega ) call hoga  ko call karega
        print(" This is a Test thread ")
t1=MyThread()
t1.test()
for i in range(1,11):
    time.sleep(0.5)
    print("this is Main Thread.!!")


#     This is a Test thread 
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