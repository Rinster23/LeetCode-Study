# 多进程启动时需要放在 if __name__ == '__main__'中
# if name == 'main’的意思是：当.py文件被直接运行时，if name == 'main’之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if name == 'main’之下的代码块不被运行。
# 有三种模式，windows是spawn
import time
import multiprocessing


# def task(arg):
#     time.sleep(2)
#     print(arg)
#
#
# if __name__ == '__main__':
#     multiprocessing.set_start_method("spawn")
#     # args 是一个元组，给task传参
#     # 元组中只有一个元素时，后面要加逗号
#     p = multiprocessing.Process(target=task, args=('xxx',))
#     p.start()  # 当前进程准备就绪，等待被CPU调度(工作单元其实是进程中的线程)
#     p.join()  # 等待当前进程的任务执行完毕后再向下继续执行。
#     # p.daemon(False) 主进程等不等子进程 False等待子进程结束再结束
#     print("继续执行...")

# import os
# import time
# import threading
# import multiprocessing
#
#
# def func():
#     time.sleep(3)
#
#
# def task(arg):
#     for i in range(10):
#         t = threading.Thread(target=func)
#         t.start()
#     print(os.getpid(), os.getppid())
#     print("线程个数",len(threading.enumerate()))
#     time.sleep(2)
#     print("当前进程的名称:", multiprocessing.current_process().name)

# if __name__ == '__main__':
#     print(os.getpid())
#     multiprocessing.set_start_method("spawn")
#     p = multiprocessing.Process(target=task, args=('xxx',))
#     p.name ="哈哈哈哈"
#     p.start()
#     print("继续执行...")

# import multiprocessing
#
# print(multiprocessing.cpu_count())
#
#
################################################################
# #数据共享
# def task(data):
#     data.append(666)
#
#
# if __name__ == '__main__':
#     data_list = []
#     p = multiprocessing.Process(target=task, args=(data_list,))
#     p.start()   # 是在子进程里面的data_list添加
#     p.join()
#     print("主进程:", data_list)  # []

# # 使用 manager
# from multiprocessing import Process, Manager
#
#
# def f(d, l):
#     d[l] = 1
#     d['2'] = 2
#     d[0.25] = None
#     l.append(666)
#
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         d = manager.dict()
#         l = manager.list()
#         p = Process(target=f, args=(d, l))
#         p.start()
#         p.join()
#         print(d)
#         print(l)

# # 使用队列queue
# import multiprocessing
#
#
# def task(q):
#     for i in range(10):
#         q.put(i)
#
#
# if __name__ == '__main__':
#     queue = multiprocessing.Queue()
#     p = multiprocessing.Process(target=task, args=(queue,))
#     p.start()
#     p.join()
#
#     print('主进程')
#     print(queue.get())  # 1
#     print(queue.get())  # 2
#     print(queue.get())  # 3

# 进程锁 多个进程共享同一个资源，抢占式做某些操作会导致问题
# import time
# import multiprocessing
#
#
# def task(lock):
#     print("开始")
#     lock.acquire()
#     # 假设文件中保存的内容就是一个值:10
#     with open('f1.txt', mode='r', encoding='utf-8') as f:
#         current_num = int(f.read())
#     print("排队抢票了")
#     time.sleep(0.5)
#     current_num -= 1
#     with open('f1.txt', mode='w', encoding='utf-8') as f:
#         f.write(str(current_num))
#     lock.release()
#
#
# if __name__ == '__main__':
#     multiprocessing.set_start_method("spawn")
#     lock = multiprocessing.RLock()  # 进程锁
#     for i in range(10):
#         p = multiprocessing.Process(target=task, args=(lock,))  # spawn下进程锁可以被传参，线程锁不行
#         p.start()
#     # spawn,需要sleep
#     time.sleep(7)

# 进程池
# import time
# from concurrent.futures import ProcessPoolExecutor
#
#
# def task(num):
#     print("执行", num)
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(4)
#     for i in range(10):
#         pool.submit(task, i)
#     pool.shutdown(True)  # 等待进程池中的任务都执行完毕后，再继续往后执行
#     print(1)

import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


def task(num):
    print("子任务", multiprocessing.current_process().pid)
    print("执行", num)
    time.sleep(2)
    return num


def done(res):
    print(multiprocessing.current_process().pid)
    time.sleep(1)
    print(res.result())
    time.sleep(1)


if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    for i in range(10):
        fur = pool.submit(task, i)
        fur.add_done_callback(done)  # done的调用由主进程处理 (与线程池不同)
    print(multiprocessing.current_process().pid)
    pool.shutdown(True)
