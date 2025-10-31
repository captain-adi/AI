import multiprocessing
import time

def work(task_name, duration):
    print(f"Starting {task_name}")
    time.sleep(duration)
    print(f"Completed {task_name}")

if __name__ == "__main__":
    start = time.time()

    # Create 2 processes
    p1 = multiprocessing.Process(target=work, args=("Task 1", 3))
    p2 = multiprocessing.Process(target=work, args=("Task 2", 3))

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    end = time.time()
    print("All tasks completed in", round(end - start, 2), "seconds")
