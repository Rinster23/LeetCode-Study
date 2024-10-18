# strings are arrays
from collections import defaultdict

import numpy as np

b = "Hello"
print(b[-5:-1])  # -1 not included

# The strip() method removes any whitespace from the beginning or the end
# The replace() method replaces a substring with another string 替换所有的
b.replace("e", " ", 1)  # 可以指定换多少个
# Note that strings are immutable so a.replace(...) created a new string.
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']
# merge
a = 'after' + 'noon'

# Use the format() method to insert numbers into strings:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

a = 'tttxqtxttttxqttxtqtxq'
print(a.count('txq'))  # 3, times txq appears
print(a.find('txq'))  # position where txq first appears if not any returns -1
# print(a.index('txqterger'))  # position where txq first appears if not any: exception
# rfind, rindex returns last position where it was found

# list
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])  # [2,5)


# add elements: append, a.insert(position, sth)
# delete elements: pop(posi) or pop() remove last one by def; remove(sth); del lista[posi];
# lista.clear() remove all elements
# merge two lists lista.extend(listb) or lista+listb

# list comprehension  newlist = [expression for item in iterable if condition == True]

# customize sort function:
def myfunc(n):
    return abs(n - 50)


# b = sorted(a)  # not in place
# a.sort()  # in place
# print(sum(a))
this_list = [100, 50, 65, 82, 23]
this_list.sort(key=myfunc)
print(this_list)

# copy lists
list_a = ['ttt', 'txq']
# list_b = list_a
# list_b.append('fy')
# print(list_a)   # 同时改变list_a
list_c = list_a.copy()  # same as list_c = list(list_a)
list_c.append('fy')
print(list_a)  # 这样不改变list_a

# tuples are ordered but unchangeable. whenever want to change a tuple, turn it into
# a list first, change the list and then trun it back to tuple
# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

# If the number of variables is less than the number of values, you can add
# an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

# join tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple2 * 2)  # (1,2,3,1,2,3)

# set unordered and unchangeable do not allow duplicates
# True and 1 is considered the same value
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)  # add elements of another set
mylist = ["kiwi", "orange"]  # add anything iterable
thisset.update(mylist)
# delete elements
# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.
# You can also use the pop() method to remove an item, but this method will remove a random item.
# join two sets:
# You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another

# keep common elements
# The intersection_update() method will keep only the items that are present in both sets,
# while The intersection() method will return a new set

# Dictionary is ordered, changeable and do not allow duplicates. Duplicate values will overwrite existing values
# keys() method will return a list of all the keys in the dictionary; return type is not list
# values() method will return a list of all the values in the dictionary; return type is not list
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
print(car.get("year"))
# if "model" in car
# delete key&value
car.pop("model")  # or del car["model"]
# copy: dict(dict_a) or dict_a.copy()


# function parameters
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments

# lambda 匿名函数
x = lambda a, b: a * b
print(x(5, 6))


def myfunc(n):
    return lambda a: a * n  # 返回一个函数


mydoubler = myfunc(2)
print(mydoubler(11))

# memoryview
data = bytearray((1, 5, 79, 100))
dataSlice = data[0:4]
data[2] = 200
assert (200 == data[2])
assert (200 != dataSlice[2])

# This is very useful when the data we're dealing with is very large
# and copying it every time we want a slice is computationally wasteful.
data = bytearray((1, 5, 79, 100))
dataSlice = memoryview(data)
print(dataSlice)
data[2] = 200  # 同步修改原列表和切片
assert (200 == data[2])
assert (200 == dataSlice[2])


# class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.__graduationyear = year  # private instance variable

    def getAge(self):
        return self.__graduationyear


x = Student("Mike", "Olsen", 2019)


# super() function that will make the child class inherit all the methods and properties from its parent


class Vehicle:
    def __init__(self, numWheels):
        self.__numWheels = numWheels

    def getNumWheels(self):
        return self.__numWheels


class Car(Vehicle):

    def __init__(self, cartype):
        numWheels = 4
        super().__init__(numWheels)
        self.__cartype = cartype

    def getType(self):
        return self.__cartype


# iterator
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.
# All these objects have an iter() method which is used to get an iterator:
mystr = "banana"
myit = iter(mystr)
results = []
while True:
    value = next(myit, None)  # 如果传入第二个参数, 获取最后一个元素之后, 下一次next返回该默认值, 而不会抛出StopIteration
    if value is None:
        break
    results.append(value)


# Strings are also iterable objects
# To create an object/class as an iterator you
# have to implement the methods __iter__() and __next__() to your object.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


# polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()  # move方法 多态

# There is a built-in function to list all the function names (or variable names) in a module.
# The dir() function:
import platform

x = dir(platform)
print(x)

# dates
import datetime

x = datetime.datetime.now()
print(x)  # 2023-07-16 15:06:21.103638
print(x.year)
print(x.strftime("%A"))  # sunday
x = datetime.datetime(2020, 5, 17)  # 2020-05-17 00:00:00
print(x.strftime("%x"))  # 05/17/20

# jason
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# convert into JSON:
y = json.dumps(x)

import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
# format results
json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)

# try except
try:
    print(hahaha)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")
else:
    print("Nothing went wrong")
#   The finally block, if specified, will be executed regardless if the try block raises an error or not.
finally:
    print("The 'try except' is finished")

# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")
# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# string formatting
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))

s = 499.93172
print('输出字符串%s' % ("absc"))
print('输出%20s' % s)  # s位宽为20，且右对齐
print('输出%-20s哈哈哈哈' % s)  # s位宽为20，且左对齐
print('输出整数%d' % s)
print('输出浮点数：%f' % s)  # 浮点数
print('输出浮点数：%8.2f' % s)  # .2：保留两位小数:8：总共所占位宽为8且为右对齐
print('12的八进制%o' % 12)  # %o八进制表示
print('172的十六进制%x' % 172)  # %x十六进制表示
print('172的十六进制%X' % 172)  # %X十六进制表示,字母大写
print('12.3科学计数法%e' % 12.3)  # %e科学计数法表示 1.230000e+01
print('12.3科学计数法%.2E' % (12.3))  # %E科学计数法表示且E大写，%.2E保留小数点后两位 1.23E+01

i = 500
print('%07d' % i)  # print a value, i = 500 padded with four leading zeroes

name = "Lee"
print("Hello, %s. Welcome home!" % name)

strs = ["dog", "date", "daf", "dar"]
for a in zip(*strs):
    print(a)

# d = dict()
# for aName in ["Bob", "Steve", "Ellen", "Bob"]:
#     d[aName] = d.get(aName, 0) + 1  # key不存在返回0

d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print("Dictionary with values as list:")
print(d)

e = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]
for i in L:
    # The default value is 0
    e[i] += 1

l = [(12, 12), (34, 13), (100, 28), (9, -10), (12, 27)]
l.sort(key=lambda x: (x[0], -x[1]))  # 先按第一个升序排序，再按第二个降序（第一个一样大的话）

# map(function, iterable) 将iterable 中每个元素传入 function，返回包含每次function函数返回值的新列表。
# reduce() 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

# str_list = ["hello", "goodbye", "--nruns=49", "farewell", "--name=Bob"]
# ans = dict([item.split("=") for item in filter(lambda x: x[:2] == "--", str_list)])
# print(ans)
from functools import reduce

print(reduce(lambda x, y: x + y, [[1, 2, 3], [4, 5], [6]]))

d = {2: 3, 4: 0, 3: 9, 1: 4}
print(sorted(d.items(), key=lambda x: x[1], reverse=True))  # sort by value

import numpy as np
import re

print('aaa'.count('aa'))  # 1
# print(len(re.findall('(?=111)', '111010101111')))  # 3

# L0 = [1, 3, 17]
# L1 = L0
# print(L1 == L0, L1 is L0)  # True,True
# L0.pop(0)
# print(L1 == L0, L1 is L0)  # True,True
# L0 = [5, 10] + L0
# print(L1 == L0, L1 is L0)  # 做了拼接，地址改变 False False
# L1.insert(0, 10)
# L1.insert(0, 5)
# print(L1 == L0, L1 is L0)  # True, False

s = "   a good   math   example  "
print(s.split())
print(" ".join(s.split()))  # 空格分开

a = [1, 1, 2, 3, 2, 4, 5, 5]
print(a.index(2, 2))  # 2

s = "caaaa"
s = s.replace("a", "T", 2)  # cTTaa
print(s.index('a'))  # 3
print(list(s))
print(sorted(s))  # ['T', 'T', 'a', 'a', 'c'] 按照ascii码排序

points = [[10, -2], [2, 8], [1, 6], [7, 12]]
print(sorted(points))  # 默认按照第一个元素排序

import bisect

ls = [1, 3, 4, 4, 6]
# bisect.bisect_right 和 bisect.bisect等价
# bisect.bisect_right 返回大于x的第一个下标
# bisect.bisect_left 返回大于等于x的第一个下标
print(bisect.bisect(ls, 4))  # 4
print(bisect.bisect_left(ls, 4))  # 2

cc = '//fe///f/3f/////ewf'
print(cc.split('/'))  # ['', '', 'fe', '', '', 'f', '3f', '', '', '', '', 'ewf']

my_list = [1, 2, 3]
ind = 4
if ind < len(my_list) and my_list[ind] > 100:  # 不会报错，前面false就不会继续了
    print("Done!")

from collections import Counter

a = '..'
if re.search('[a-zA-Z]', a):
    print('yes')

s = 'abc'
print(list(map(s.index, list(s))))  # [0, 1, 2]

dic_a = {'a': 4, 'b': [1, 2, 3]}
dic_b = {'a': 100, 'c': 70}
dic_a.update(dic_b)
print(dic_a.values())  # dict_values([100, [1, 2, 3], 70])
