import threading
import time
def print_numbers():
    for i in range(5):
        print(f"{threading.current_thread().name}:{i}")
        time.sleep(1)

def cherry():
    for i in range(6,10):
        print(f"{threading.current_thread().name}:{i}")
        time.sleep(1 )


thread1=threading.Thread(target=print_numbers,name="thread-1")
thread2=threading.Thread(target=cherry,name="thread-2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("both threads execution is completed")
