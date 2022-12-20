import threading
import time

def eat_popcorn():
    time.sleep(4)
    print("Eating popcorn!")
    
def watch_movie():
    time.sleep(3)
    print("Watching movie")
    
def drink_cola():
    time.sleep(5)
    print("Drinking cola!")
    
e = threading.Thread(target=eat_popcorn)
e.start()

w = threading.Thread(target=watch_movie)
w.start()

d = threading.Thread(target=drink_cola)
d.start()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())