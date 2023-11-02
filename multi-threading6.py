# 2--class base thread
import threading
import time


# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(1,11):
#             time.sleep(1)   # execute hone me (1) second ka time lega
#             print("This is Child Thread....!")
# t1=MyThread()
# t1.start()
# t1.join()  # join() funtion se first---( child thread call hoga )start hoga bad me ----(main thread)
# for i in range(1,11):
#     time.sleep(0.5)     # execute hone me (0.5) second ka time lega
#     print("this is Main Thread.!!")

# OUTPUT

# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
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

# ---------------------------------

# if again call -- t1.start() dobara so given error only 1 time call by object

# 2--class base thread
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(1,11):
            time.sleep(1)
            print("This is Child Thread....!")
t1=MyThread()
# t1.start()
# t1.join()
t1.run()            # normal function ki tarah hi call hoga - pahle child thread - phir main thread hoga
for i in range(1,11):
    time.sleep(0.5)
    print("this is Main Thread.!!")
# t1.start()             # you don't call ---- t1.start()  only 1 bar call kar sakte hai bas 
                    #  NOTE- dusra object  banakr call kar sakte hai ---t2.star() hum kar sakte hai 



# raise RuntimeError("threads can only be started once")
# RuntimeError: threads can only be started once
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!
# This is Child Thread....!