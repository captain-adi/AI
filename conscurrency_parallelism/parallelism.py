from multiprocessing import Process
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)   # simulate heavy calculation
    print(f"Finished {name}")

start = time.time()

p1 = Process(target=task, args=("Task 1",))
p2 = Process(target=task, args=("Task 2",))

p1.start()
p2.start()
p1.join()
p2.join()

end = time.time()
print("Time taken:", end - start)
