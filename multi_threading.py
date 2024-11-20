'''
Multi Threading:it is a way to run multiple threads conncurrently.
                allowing the execution of tasks in parallel,pythons threading mobile provides a way to work with threads
                which can help improve performance,especially in I/o  bound tasks.
                A lightweight process that runs in the background and can execute tasks concurrently.



'''
import threading
import time
def print_numbers():
    for i in range(5):
        print(f"{threading.current_thread().name}:{i}")
        time.sleep(1)

thread1=threading.Thread(target=print_numbers,name="thread-1")
thread2=threading.Thread(target=print_numbers,name="thread-2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("both threads execution is completed")
