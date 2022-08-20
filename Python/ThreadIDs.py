import threading
import multiprocessing
import time
import os

def thread_test(name):

    print(f"{name} Proc ID: {str(os.getpid())} Thread ID: {str(threading.get_native_id())}")
    
    time.sleep(5) # delay so that it doesn't end right away, adjust to catch in (h)top

def spawn_thread(name):
    for i in range (3):
        thread = threading.Thread(target=thread_test, args=[f"{name}{i}"])
        thread.start()

thread_test("Main ")
spawn_thread("Thr#")
process1 = multiprocessing.Process(target=spawn_thread, args=["Pr1:"])
process1.start()
process2 = multiprocessing.Process(target=spawn_thread, args=["Pr1:"])
process2.start()

#Example output
#Main  Proc ID: 164610 Thread ID: 164610
#Thr#0 Proc ID: 164610 Thread ID: 164627
#Thr#1 Proc ID: 164610 Thread ID: 164628
#Thr#2 Proc ID: 164610 Thread ID: 164629
#Pr1:0 Proc ID: 164630 Thread ID: 164631
#Pr1:1 Proc ID: 164630 Thread ID: 164633
#Pr1:2 Proc ID: 164630 Thread ID: 164634
#Pr1:0 Proc ID: 164632 Thread ID: 164635
#Pr1:1 Proc ID: 164632 Thread ID: 164636
#Pr1:2 Proc ID: 164632 Thread ID: 164637