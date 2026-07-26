# import sys
# import timeit
# from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
# from itertools import (
#     product,
#     permutations,
#     combinations,
#     combinations_with_replacement,
#     accumulate,
#     groupby,
#     count,
#     cycle,
#     repeat,
# )
# from functools import reduce
# import operator

# mylist = [1, 2, 3, 4, 5]
# a = [i * i for i in mylist]
# print(mylist)
# print(a)

# my_tuple = ("a", "p", "p", "l", "e")

# print(my_tuple.count("p"))
# print(my_tuple.index("l"))

# tuple1 = (1, 2, 3, 4, 5)
# i1, *i2, i3 = tuple1
# print(i1)
# print(i2)
# print(i3)

# my_tuple2 = (1, 2, 3, 4, 5)
# print(sys.getsizeof(mylist), "bytes")
# print(sys.getsizeof(my_tuple2), "bytes")

# print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
# print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))


# my_dict = {"name": "ali", "age": 27}
# my_dict2 = dict(name="ali", age=45)
# print(my_dict)
# print(my_dict2)

# my_dict.pop("age")
# my_dict2.popitem()
# print(my_dict)
# print(my_dict2)

# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     print(key)
#     print(value)


# CONVERT LIST TO STRING
# new_string = " ".join(my_list)
# print(new_string)

# a = "aaabbccccc"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.most_common(1))

# point = namedtuple("Point", "x,y")
# pt = point(1, -4)
# print(pt.x, pt.y)

# Ordered_dict = OrderedDict()
# Ordered_dict["a"] = 1
# Ordered_dict["c"] = 2
# Ordered_dict["d"] = 3
# Ordered_dict["b"] = 4
# print(Ordered_dict)

# d = defaultdict(int)
# d["a"] = 1
# d["b"] = 2
# print(d["c"])

# d = deque()
# d.append(1)
# d.append(3)
# d.extendleft([5, 6, 7, 8, 9])
# print(d)
# d.rotate(2)
# print(d)


# a = [1, 2]
# b = [3]
# prod = product(a, b, repeat=2)
# print(list(prod))


# a = [1, 2, 3]
# perm = permutations(a, 2)
# print(list(perm))

# a = [1, 2, 3, 4]
# comb = combinations(a, 2)
# print(list(comb))
# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))

# a = [1, 2, 5, 3, 4]
# acc = accumulate(a, func=operator.mul)
# print(a)
# print(list(acc))
# acc = accumulate(a, func=max)
# print(list(acc))


# b = [1, 2, 3, 4]


# def smaller_than_3(x):
#     return x < 3


# group_obj = groupby(b, key=smaller_than_3)
# for key, value in group_obj:
#     print(key, list(value))


# person = [
#     {"name": "tim", "age": 25},
#     {"name": "dan", "age": 25},
#     {"name": "lisa", "age": 27},
#     {"name": "claire", "age": 28},
# ]

# group_obj = groupby(person, key=lambda x: x["age"])
# for key, value in group_obj:
#     print(key, list(value))

# for i in count(10):
#     print(i)
# for i in cycle(a):
#     print(i)

# for i in repeat(1, 3):
#     print(i)

# add10 = lambda x: x + 10
# print(add10(5))


# points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# points2D_sorted = sorted(points2D, key=lambda x: x[1])
# print(points2D)
# print(points2D_sorted)


# a = [1, 2, 3, 4, 5]
# b = map(lambda x: x * 2, a)
# print(list(b))
# # achieve same goal
# c = [x * 2 for x in a]
# print(c)

# a = [1, 2, 3, 4]
# product_a = reduce(lambda x, y: x * y, a)
# print(product_a)

# x = -5
# if x < 0:
#     raise Exception("x sould be positive")
# assert x >= 0, "x is not prositive"

# try:
#     a = 5 / 0
#     b = 5 + "ta"
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("every thing is fine")
# finally:
#     print("cleaning up ...")


# class ValueTooHighError(Exception):
#     pass


# class ValueTooSmallError(Exception):
#     def __init__(self, message, value):
#         self.message = message
#         self.value = value


# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError("value is too high")
#     if x < 5:
#         raise ValueTooSmallError("value is too small", x)


# try:
#     test_value(1)
# except ValueTooHighError as e:
#     print(e)
# except ValueTooSmallError as e:
#     print(e.message, e.value)

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)
# logging.debug("this is a debug message")
# logging.info("this is an info message")
# logging.warning("this is a warning message")
# logging.error("this is an error message")
# logging.critical("this is a critical message")
# import helper
