import time
import threading
def download(file):
    print(f"downloading {file}...")
    time.sleep(2)
    print(f"{file} download finished  .")

start = time.time()
d1 = threading.Thread(target=download,args=("file1",))
d2 = threading.Thread(target=download,args=("file2",))

d1.start()
d2.start()

d1.join()
d2.join()
end = time.time()
print(f"time taken for download : " , end - start)