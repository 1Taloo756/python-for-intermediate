import sys


def mygenerator():
    yield 1
    yield 3
    yield 2


g = mygenerator()

# for i in g:
#     print(i)

# value = next(g)
# print(value)
# value = next(g)
# print(value)

print(sum(g))

print(sorted(g))


def countdown(num):
    print("starting")
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)
value = next(cd)


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for i in fib:
    print(i)


mygenerator = (i for i in range(100000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(100000) if i % 2 == 0]
print(sys.getsizeof(mylist))
