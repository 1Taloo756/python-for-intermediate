import copy

org = [[0, 1, 2, 3], [4, 5, 6]]
# cpy = copy.copy(org) shallow copy
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person("Alen", 30)
p2 = copy.copy(p1)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)

company_clone.boss.age = 70
print(company_clone.boss.age)
print(company.boss.age)
