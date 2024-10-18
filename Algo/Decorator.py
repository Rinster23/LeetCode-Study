# nonlocal 声明
# 与 global 声明类似，nonlocal 声明可以在闭包中声明使用上一级作用域中的变量
# nonlocal通常用于嵌套函数
def foo():
    a = 0

    def bar():
        nonlocal a
        a += 1
        return a

    return bar


# a = 1
# def fun():
#     print(a) # 在函数内部找不到对 a 的定义，则去外层查询。输出1。
# fun()

# a = 1
# def fun():
#     print(a) # 先引用
#     a = 2 # 再修改 报错是referenced before assigned, 已经知道a是局部变量了
# fun()

# a = 1
# def fun():
#     global a # a为全局变量 这里不能换成nonlocal 一旦外层变量是全局变量，则只能用 global
#     print(a) # 输出1
#     a = 2 # 改变的是全局变量，因此出了这个局部作用域，仍然有效
# fun()
# print(a) # 输出2

# def outer_fun():
#     a = 1
#     def fun():
#         nonlocal  a # a为外层变量 这里不能换成global
#         print(a) # 输出1
#         a = 2
#     fun()
#     print(a) #输出2
# outer_fun()

def outer_fun():
    a = 1

    def fun():
        global a  # a为全局变量，与上面等于1的 a 没有关系
        a = 3  # 定义全局变量
        print(a)  # 输出3
        a = 2

    fun()
    print(a)  # 输出1，局部变量


outer_fun()
print(a)  # 输出2，全局变量

# 内嵌函数作为返回值传递给外部变量时，将会把定义它时涉及到的引用环境和函数体自身复制后打包成一个整体返回
# c 变量对应的闭包包含两部分，变量环境 a = 0 和函数体 a = a + 1
# c = foo()
# print(c())  # 1
# print(c())  # 2


# def a_new_decorator(a_func):
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
#
# @a_new_decorator
# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration")
#
#
# a_function_requiring_decoration()  # 等价于不用@, a_new_decorator(a_function_requiring_decoration)()
# print(a_function_requiring_decoration.__name__)  # wrapTheFunction

########################################################################
from functools import wraps

# def a_new_decorator2(a_func):
#     # @wraps(a_func) 确保了 a_new_decorator2 的名字和文档字符串不会被 wrapper 函数wrapTheFunction覆盖。
#     # 如果没有使用 @wraps, my_function.__name__ 将显示为 'wrapTheFunction'
#     @wraps(a_func)
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#         a_func()
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
#
# @a_new_decorator2
# def a_function_requiring_decoration():
#     """Hey yo! Decorate me!"""
#     print("I am the function which needs some decoration")
#
#
# print(a_function_requiring_decoration.__name__)
# a_function_requiring_decoration()

# Output: a_function_requiring_decoration

#####################################################
# 使用@my_decorator语法时，是在应用一个以单个函数作为参数的一个包裹函数。我们可以编写一下能返回一个包裹函数的函数。
# def logit(logfile='out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             print("write data to " + logfile)
#             return func(*args, **kwargs)
#
#         return wrapped_function
#
#     return logging_decorator
#
#
# @logit(logfile="txq data")  # ()!!!
# # 这等价于 @logging_decorator
# def testfunc1(a, b):
#     print(a, b)
#     print("Done!")
#
#
# testfunc1(3, 8)

#################################################################
import warnings


def type_check(at_mismatch='warning'):
    def decorator(func):
        # Extracting the expected types from default values
        expected_types = {k: type(v) for k, v in func.__kwdefaults__.items()}

        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg, value in kwargs.items():
                expected_type = expected_types.get(arg)
                if expected_type and not isinstance(value, expected_type):
                    message = f"Type mismatch for argument '{arg}': expected {expected_type.__name__}, got {type(value).__name__}"
                    if at_mismatch == 'warning':
                        warnings.warn(message)
                    elif at_mismatch == 'exception':
                        raise TypeError(message)
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Usage examples:

@type_check()
def some_func1(m, n, *, a=6, b='cc'):  # 这意味着在 * 之后声明的任何参数都必须以关键字参数的形式传递，而不能作为位置参数。
    print(a,b)


some_func1(3, 2, a=10, b='900')

# @type_check(at_mismatch='exception')
# def some_func2(*, a=7, b='dd'):
#     pass


