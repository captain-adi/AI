import threading
import time

def boil_milk():
    print(f" {threading.current_thread().name} started boiling milk ")
    time.sleep(2)  # Simulate time taken to boil milk
    print(f" {threading.current_thread().name} finished boiling milk ")

def toast_bread():
    print(f" {threading.current_thread().name} started toasting bread ")
    time.sleep(1)  # Simulate time taken to toast bread
    print(f" {threading.current_thread().name} finished toasting bread ")

start = time.time()
t1 = threading.Thread(target=boil_milk, name="BoilMilkThread")
t2 = threading.Thread(target=toast_bread, name="ToastBreadThread")

t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()

print(f"time taken : {end - start}")