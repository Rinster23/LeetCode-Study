from multiprocessing import Process, current_process, Lock, Queue, Pool
import time


def sell_ticket(queue: Queue, lock):
    print(current_process().name + ' ready to get ticket')
    # while queue.qsize() > 0:
    #     time.sleep(1)  # 在这里停一秒，程序跑完后不终止
    #     # 因为会有多个进程同时进入这里，都去取票
    #     # 如果仅剩一张票，多个进程同时进入这里，只有一个进程能取到票
    #     # 其他进程会阻塞因为没票了，所以程序不结终止
    #     # 所以要加个锁
    #     ticket = queue.get()
    #     print(current_process().name + ' get ticket: ' + str(ticket))
    #     print(str(queue.qsize()) + ' tickets left')
    #     time.sleep(1)  # 这里停一秒让更多进程参与进来

    while queue.qsize() > 0:
        time.sleep(1)
        with lock:
            if not queue.empty():
                ticket = queue.get()
                print(current_process().name + ' get ticket: ' + str(ticket))
                print(str(queue.qsize()) + ' tickets left')


if __name__ == '__main__':
    lock = Lock()
    tickets = list(range(1, 50))
    queue = Queue(maxsize=50)
    for i in tickets:
        queue.put(i)  # 有阻塞，如果满了就等待
        # queue.put_nowait(i) # 如果满了就报错
    for _ in range(5):
        Process(target=sell_ticket, args=(queue, lock)).start()

