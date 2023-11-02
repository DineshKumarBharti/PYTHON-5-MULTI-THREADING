#1-funtion base thread

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
for i in range(1,11):
    print("Main Thread..!!!!!")


# OUTPUT
# This is Task1..!This is Task2...!!
# Main Thread..!!!!!
# This is Task1..!
# Main Thread..!!!!!
# This is Task1..!
# Main Thread..!!!!!
# This is Task1..!
# Main Thread..!!!!!
# This is Task1..!
# Main Thread..!!!!!
# This is Task1..!
# Main Thread..!!!!!
# Main Thread..!!!!!
# This is Task2...!!
# This is Task2...!!
# This is Task2...!!
# Main Thread..!!!!!
# This is Task1..!
# Main Thread..!!!!!
# This is Task1..!
# This is Task1..!
# This is Task1..!
# This is Task2...!!
# This is Task2...!!
# This is Task2...!!
# Main Thread..!!!!!
# This is Task2...!!

# This is Task2...!!
# This is Task2...!!