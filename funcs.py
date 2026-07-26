def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)


def poo(a, b, *, c, d):
    print(a, b, c, d)


poo(1, 2, d=4, c=3)


def soo(a, b, c):
    print(a, b, c)


my_list = [1, 2, 3]
soo(*my_list)


def doo(a, b, c):
    print(a, b, c)


my_dict = {"a": 1, "b": 2, "c": 3}
doo(**my_dict)


def zoo():
    global number
    number = 3


number = 0
zoo()
print(number)
