"""
Learning Dictionaries
"""

from collections import OrderedDict

contacts = {
    "Anoop": {"phone": "123123312", "email": "bla@gmail.com"},
    "Akila": {"phone": "121322313", "email": "bla@gmail.com"},
}

print(contacts["Anoop"]["phone"])

names = dict(name="Anoop", age=34)
print(names)
print(names.get("akila", None))

numbers = OrderedDict({"1": 1, "2": 2, "4": 4, "3": 3})
print(numbers)

for key, value in contacts.items():
    print(key, "=", value)

print("Anoop" "Akila")
