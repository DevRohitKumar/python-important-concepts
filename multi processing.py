# Multi processing 🎛️
# multi processing is cpu based unlike multi threading which is I/O based

import time
from multiprocessing import Process, cpu_count

def counter(number):
    count = 0
    while count < number:
        count += 1


def main():
    
    a = Process(target=counter, args=(50000000,))
    b = Process(target=counter, args=(50000000,))
    c = Process(target=counter, args=(50000000,))
    d = Process(target=counter, args=(50000000,))
    e = Process(target=counter, args=(50000000,))
    f = Process(target=counter, args=(50000000,))
    
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    
    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    
    print("Time taken: ", time.perf_counter())


if __name__ == "__main__":
    main()