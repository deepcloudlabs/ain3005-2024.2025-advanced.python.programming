from threading import Thread, Lock

data = 0 # shared memory
lock = Lock()

def fun(limit):
    global data
    with lock:
        total=data
        for i in range(limit):
            total+=1
        data = total
threads = []
for i in range(10):
    thread = Thread(target=fun, args=(1_000_000,))
    threads.append(thread)
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(data)
