
# 2--class base thread
import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(1,11):
            print("This is Child Thread....!")
t1=MyThread()
t1.start()
for i in range(1,11):
    print("this is Main Thread.!!")


# output 

# This is Child Thread....!this is Main Thread.!!

# This is Child Thread....!this is Main Thread.!!

# This is Child Thread....!this is Main Thread.!!

# this is Main Thread.!!
# This is Child Thread....!this is Main Thread.!!
# This is Child Thread....!

# this is Main Thread.!!This is Child Thread....!
# this is Main Thread.!!

# this is Main Thread.!!
# This is Child Thread....!
# this is Main Thread.!!
# This is Child Thread....!
# this is Main Thread.!!
# This is Child Thread....!
# This is Child Thread....!


