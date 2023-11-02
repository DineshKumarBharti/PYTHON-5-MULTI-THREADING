import threading
def task1():
    for i in range(1,11):
        print("This is Task1..!")
def task2():
    for i in range(1,11):
        print("This is Task2...!!")
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()

# OUTPUT- 1 -mixed output given one to one both task1& task2
#         2-if you run again and again so it will give diffrent-2 result everytime not same result given

# This is Task1..!
# This is Task1..!
# This is Task2...!!
# This is Task1..!This is Task2...!!

# This is Task1..!This is Task2...!!

# This is Task2...!!This is Task1..!
# This is Task1..!

# This is Task2...!!This is Task1..!

# This is Task2...!!This is Task1..!

# This is Task2...!!
# This is Task1..!
# This is Task2...!!
# This is Task2...!!
# This is Task1..!This is Task2...!!
