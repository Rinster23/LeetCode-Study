import sys

list0 = [1] * 100
list1 = [1] * 1000000
print(sys.getsizeof(list0))
print(sys.getsizeof(list1))
# 如果我们要处理更多元素，那么所占内存就呈线性增大，所以受到内存限制，列表容量是有限的。
# 通常我们并不会一次处理所有元素，而只是集中在其中的某些相邻的元素上。
# 所以如果列表元素可以用某种算法用已知量推导出来，就不必一次创建所有的元素。
# 这种边循环边计算的机制，称为生成器（generator），生成器是用时间换空间的典型实例。

# generator expression
gen0 = (x * x for x in range(5))
print(gen0)  # 不能像list一样被打印出来
gen1 = (x * x for x in range(5000000))
print(sys.getsizeof(gen0))
print(sys.getsizeof(gen1))  # 两个分配的内存一样大


# generator是可迭代对象，用for in 遍历

# 通过生成器表达式来生成 generator 是有局限的，比如斐波那契数列用表达式写不出来，复杂的处理需要生成器函数完成。
# 生成器函数

def fib_generator(n):
    i, j = 0, 1
    while i < n:
        yield i
        i, j = j, i + j


print(type(fib_generator))  # <class 'function'>
print(type(fib_generator(5)))  # <class 'generator'>

# 可迭代对象，需要提供 __iter__()方法，否则不能被 for 语句处理。
# 迭代器必须同时实现 __iter__() 和 __next__()方法，
# __next__() 方法包含了用户自定义的推导算法，这是迭代器对象的本质。
# 生成器表达式和生成器函数产生生成器时，会自动生成名为 __iter__ 和 __next__ 的方法。
