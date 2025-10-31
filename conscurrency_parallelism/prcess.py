from multiprocessing import Process
import time 

def cup_heavy():
    print(" started preparing heavy CUP task")
    total = 0 
    for i in range(10**9):
        total += i
    print(" finished preparing heavy CUP task")
    print(f"Total: {total}")

if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cup_heavy) for _ in range(2)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end = time.time()
    print(f"Total time taken: {end - start} seconds")