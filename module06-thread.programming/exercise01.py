import threading

# Process' Data
data = 0
# text
def task(limit):
    global data
    # stack/temp/local/automatic
    total = data
    for i in range(limit):
        total += 1
    data = total
threads = []
for i in range(10):
    thread = threading.Thread(target=task, args=(10_000_000, ))
    threads.append(thread)
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(data)
