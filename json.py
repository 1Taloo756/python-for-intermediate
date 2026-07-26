import json

# person = {
#     "name": "john",
#     "age": 30,
#     "city": "New York",
#     "hasChildren": False,
#     "tittles": ["engineer", "programmer"],
# }

# personJSON = json.dumps(person, indent=4)
# print(personJSON)

# with open("person.json", "w") as file:
#     json.dump(person, file)
# person = json.loads(personJSON)
# print(person)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 59)


def encoder_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Type error")


userJSON = json.dumps(user, default=encoder_user)


from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


userJSON = UserEncoder().encode(user)

print(userJSON)


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
