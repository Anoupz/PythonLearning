"""
Learning Dictionaries
"""

from collections import OrderedDict

contacts = {
    "Test1": {"phone": "123123312", "email": "bla@gmail.com"},
    "test2": {"phone": "121322313", "email": "bla@gmail.com"},
}

print(contacts["Test1"]["phone"])

names = dict(name="Test1", age=34)
print(names)
print(names.get("test2", None))

numbers = OrderedDict({"1": 1, "2": 2, "4": 4, "3": 3})
print(numbers)

for key, value in contacts.items():
    print(key, "=", value)

print("Test1" "test2")
