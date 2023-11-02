'''
class thread{
    def start (self):
    
     #--10k + code of inside ---
        run ()
    def run(self):
        pass
}
'''
import threading
def task1():
    for i in range(1,11):
        print("This is Task1..!")
def task2():
    for i in range(1,11):
        print("This is Task2...!!")
task1()
task2()

# OUTPUT- there is one thread only

# This is Task1..!
# This is Task1..!
# This is Task1..!
# This is Task1..!
# This is Task1..!
# This is Task1..!
# This is Task1..!
# This is Task1..!
# This is Task1..!
# This is Task1..!
# This is Task2...!!
# This is Task2...!!
# This is Task2...!!
# This is Task2...!!
# This is Task2...!!
# This is Task2...!!
# This is Task2...!!
# This is Task2...!!
# This is Task2...!!
# This is Task2...!!

