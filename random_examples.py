import random
import secrets
import numpy as np

# a = random.random()
# a = random.uniform(1, 10)

# a = random.randint(1, 10)
# a = random.normalvariate(0, 1)
# mylist = list("ABCDEF")
# a = random.choices(mylist, k=3)
# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))


# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))


a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4)
print(a)

mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

a = np.random.randint(3, 10, (3, 4))
print(a)
