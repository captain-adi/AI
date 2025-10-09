import threading
import time

def makeTea():
    print(f" {threading.current_thread().name} started ")
    count = 0 
    for _ in range(100_000_000):
        count += count
    print(f" {threading.current_thread().name} started ")

start = time.time()
thread1 = threading.Thread(target=makeTea,name="t1")
thread2 = threading.Thread(target=makeTea,name="t2")


thread1.start()
thread2.start()


thread1.join()
thread2.join()


end = time.time()
print(f"time taken : ", end - start)