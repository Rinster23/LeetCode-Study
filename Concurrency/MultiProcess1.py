import os
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager, Pool

# 方法一
# def task(file_name, count_dict):
#     # . . .
#     count_dict[file_name] = {'cnt': 1000, 'ip_num': 90}
#
#
# def run():
#     pool = ProcessPoolExecutor(4)
#     with Manager() as manager:
#         """
#         count_dict = {"20210322.log": {"total":10000, 'ip':800}}
#         """
#         count_dict = manager.dict()
#         for file_name in os.listdir("files"):
#             pool.submit(task, file_name, count_dict)
#         pool.shutdown(True)
#         for k, v in count_dict.items():
#             print(k, v)

# 方法二
# def task(file_name):
#     # . . .
#     return {'cnt': 1000, 'ip_num': 90}
#
#
# def outer(info, file_name):
#     def done(res, *args, **kwargs):
#         info[file_name] = res.result()
#
#     return done
#
#
# def run():
#     info = {}
#     pool = ProcessPoolExecutor(4)
#     for file_name in os.listdir("files"):
#         fur = pool.submit(task, file_name)  # 回调函数: 主进程
#         fur.add_done_callback(outer(info, file_name))
#     pool.shutdown(True)
#     for k, v in info.items():
#         print(k, v)


############################################################################
from random import random


def my_task(sub_list):
    return list(map(sum, sub_list))


def log(res, ind):
    def real(outcome, *args, **kwargs):
        res[ind] = outcome.result()

    return real


def my_run():
    pool = ProcessPoolExecutor(4)
    sub_len = 10 ** 6
    sub_num = len(my_list) // sub_len
    if len(my_list) % sub_len != 0:
        sub_num += 1
    res = [0] * sub_num
    start = 0
    for i in range(sub_num):
        if i != sub_num - 1:
            foo = pool.submit(my_task, my_list[start:start + sub_len])
        else:
            foo = pool.submit(my_task, my_list[start:])
        foo.add_done_callback(log(res, i))
        start += sub_len
    pool.shutdown(True)
    from functools import reduce
    ans = reduce(lambda x, y: x + y, res)
    return ans


def my_task2(sub_list, res_dict, ind):
    res_dict[ind] = list(map(sum, sub_list))


def my_run2():
    pool = ProcessPoolExecutor(4)
    sub_len = 10 ** 6
    sub_num = len(my_list) // sub_len
    if len(my_list) % sub_len != 0:
        sub_num += 1
    start = 0
    with Manager() as manager:
        res = manager.list([0] * sub_num)
        for i in range(sub_num):
            if i != sub_num - 1:
                pool.submit(my_task2, my_list[start:start + sub_len], res, i)
            else:
                pool.submit(my_task2, my_list[start:], res, i)
            start += sub_len
        pool.shutdown(True)
        from functools import reduce
        ans = reduce(lambda x, y: x + y, res)
        return ans


def my_run3():
    pool = Pool(5)
    start = 0
    sub_len = 10 ** 7 // 5
    # apply async 不会阻塞主进程
    temp1 = pool.apply_async(my_task, (my_list[start:start + sub_len],))
    start += sub_len
    temp2 = pool.apply_async(my_task, (my_list[start:start + sub_len],))
    start += sub_len
    temp3 = pool.apply_async(my_task, (my_list[start:start + sub_len],))
    start += sub_len
    temp4 = pool.apply_async(my_task, (my_list[start:start + sub_len],))
    start += sub_len
    temp5 = pool.apply_async(my_task, (my_list[start:start + sub_len],))
    pool.close()
    pool.join()
    return temp1.get() + temp2.get() + temp3.get() + temp4.get() + temp5.get()

def assert_equal_lists(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


if __name__ == '__main__':
    # Generating the list
    my_list = [[random(), random()] for _ in range(int(1e7))]
    # Single-processing approach
    start_time = time.time()
    result_single = list(map(sum, my_list))
    end_time = time.time()
    print("Time for single-processing approach:", end_time - start_time)
    time.sleep(10)
    start_time = time.time()
    result_multi = my_run3()
    end_time = time.time()
    print("Time for multiprocessing approach:", end_time - start_time)
    assert assert_equal_lists(result_single, result_multi)
