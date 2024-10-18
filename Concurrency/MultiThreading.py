import threading

# python GIL锁：每个进程中只能有一个线程能被cpu调度，使用多核cpu优势需要使用多进程
# 计算密集型任务---多进程
# IO密集型任务---多线程

# loop = 100000
# ans = 0
#
# def add(cnt):
#     global ans
#     for i in range(cnt):
#         ans += 1
#
# t = threading.Thread(target=add,args=(loop,))
# # t.start()
# # print(ans)  # 这里ans不是最终答案，主线程跑到这里的时候子线程可能还没有结束
#
# t.start()
# t.join()
# print(ans)  #是最终答案，join将等待当前线程的任务执行完毕再向下继续执行
#
# #######################################################################
#
# def sub(cnt):
#     global ans
#     for i in range(cnt):
#         ans -= 1
#
# t1 = threading.Thread(target=add,args=(loop,))
# t2 = threading.Thread(target=sub,args=(loop,))
# # 情形 1
# t1.start()  #线程t1准备好被cpu调度，这时候与t2无关
# t1.join()   #加法做完
# t2.start()  #线程t2准备好被cpu调度
# t2.join()   #减法做完
# print(ans) # 0
# # 情形 2
# t1.start()  #线程t1准备好被cpu调度
# t2.start()  #线程t2准备好被cpu调度
# # GIL锁，只能执行一个线程，将会t1/t2切换着运行，
# # 可能加法还没加上去就切换到减法了，减法做完之后在切换回加法时会导致减法没做，导致结果不对
# t1.join()
# t2.join()
# print(ans) # 可能不为0

#######################################################################
# t1.setDaemon(True) # 参数为True表示主线程结束后不等待子线程，立即结束程序，需要放在start方法前面
#######################################################################
# 线程安全
# lock_obj = threading.RLock()
# loop = 10000000
# ans = 0
#
#
# def add(cnt):
#     lock_obj.acquire()  # 申请锁，否则等待
#     global ans
#     for i in range(cnt):
#         ans += 1
#     lock_obj.release()  # 释放锁
#
#
# def sub(cnt):
#     lock_obj.acquire()  # 申请锁，否则等待
#     global ans
#     for i in range(cnt):
#         ans -= 1
#     lock_obj.release()  # 释放锁
#
#
# t1 = threading.Thread(target=add, args=(loop,))
# t2 = threading.Thread(target=sub, args=(loop,))
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# print(ans)
#######################################################################
# num = 0


# def task():
#     with lock_obj:  # 自动申请、释放锁
#         global num
#         for i in range(100000):
#             num += 1
#         print(num)


# for i in range(2):
#     t = threading.Thread(target=task)
#     t.start()

# 有些数据类型/方法是线程安全的，内部集成了锁，例如list.append
#######################################################################
# 线程池
from concurrent.futures import ThreadPoolExecutor
import time
import random


def task(url):
    print(url)
    time.sleep(5)
    return random.randint(0, 10)


# pool = ThreadPoolExecutor(10)  # 维护十个线程
url_list = ['www.{}'.format(i) for i in range(100)]

# for i in url_list:
#     pool.submit(task, i)
# pool.shutdown(True)  # 等线程池中的任务执行完毕再继续

#######################################################################

def log(response):
    print(response.result())


name_list = []
pool = ThreadPoolExecutor(10)  # 维护十个线程
for url in url_list:
    name = pool.submit(task, url)
    name.add_done_callback(log)  # 可以做分工
    name_list.append(name)

pool.shutdown(True)
for i in name_list:
    print(i.result())


#######################################################################
# 单例模式

# class Singleton:
#     instance = None
#     lock = threading.RLock()
#
#     def __init__(self, name):
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance:
#             return cls.instance
#         with cls.lock:
#             if cls.instance:
#                 return cls.instance
#             time.sleep(1)
#             cls.instance = object.__new__(cls)
#             return cls.instance
#
#
# def task():
#     obj = Singleton('x')
#     print(obj)
#
#
# for i in range(10):
#     t = threading.Thread(target=task)
#     t.start()  # 每个地址都一样因为上锁了，只有一个能申请到锁
#
#
######################################################################
# data.txt文件中有10000条数据，每100条创建一个线程，在线程中把当前100条数据的num列相加。表头为id,num
def task(row_list):
    num_list = [int(row.split(",")[-1]) for row in row_list]
    result = sum(num_list)
    print(result)


def run():
    file_object = open('data.txt', mode='r', encoding='utf-8')
    file_object.readline()
    row_list = []   # 1
    for line in file_object:
        row_list.append(line.strip())
        if len(row_list) == 100:
            t = threading.Thread(target=task, args=(row_list,))
            t.start()
            row_list = []  # 不要用 row_list.clear(),会把指向的内存清空从而task中读不到内容。重新赋值为[]不会改变原地址中的内容
    if row_list:
        t = threading.Thread(target=task, args=(row_list,))
        t.start()
    file_object.close()
