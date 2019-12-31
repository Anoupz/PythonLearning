# Variables with dataTypes

import turtle

my_turtle = turtle.Turtle()


def square() -> None:
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)


# Date Types

# Integer
i = 1
print(i)
# Floats
float(i)  # will convert i to float and print 1.0
print(i)
# Strings
str(i)  # this will convert i to string and print ""
print(i)
# Boolean

# strings

s = "Hello"

print("Will print first char which starts at 0--> ", s[0])

# List
# List can contain any type of data type like string, boolean, another array
arr1 = [1, 2, 3, 4]

print(arr1[1])

names = ["Anoop", "Akila", "Aditi"]
names.append("baby")
names.insert(0, "Family")
names.insert(1, "Father")
print(names)
names.reverse()
print("After reversing", names)

digits = [1, 2, 3, 4, 5, 6, 7]

print(digits[:4:2])

for i in range(len(digits)):
    print(digits[:i])

problems = "broke, pale, short, nerdy"
print(problems.split(", "))

# tuples
# tuples are immutable
t: tuple = (1, 2, 3)
print(t[0])

person1 = ("Anoop", 34, "Pizza")
person2 = ("Akila", 32, "Pizza")
name, age, fav_food = person1

print(name, age, fav_food)

persons = [person1, person2]

for name, age, fav_food in persons:
    print(name)
    print(age)
    print(fav_food)
    print()
