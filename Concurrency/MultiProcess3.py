from multiprocessing import Process, current_process, Value, Lock
import time


def get_sum(num, s, lock):
    while num.value < 101:
        with lock:
            if num.value < 101:
                s.value += num.value
                print(current_process().name, num.value)
                num.value += 1
                time.sleep(0.1)


if __name__ == '__main__':
    num = Value('i', 1)
    s = Value('i', 0)
    lock = Lock()
    p_list = []
    for _ in range(5):
        p = Process(target=get_sum, args=(num, s, lock))
        p_list.append(p)
        p.start()
    for item in p_list:
        item.join()
    print(s.value)
