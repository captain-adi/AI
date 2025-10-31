import time 
import threading


def download(url):
    print(f" {threading.current_thread().name} started downloading from {url} ")
    time.sleep(2)  # Simulate time taken to download
    print(f" {threading.current_thread().name} finished downloading from {url} ")


urls = [
    "1","2","3"
]

threads = [threading.Thread(target=download, args=(url,)) for url in urls]
for thread in threads:
    thread.start()

for t in threads:
    t.join()