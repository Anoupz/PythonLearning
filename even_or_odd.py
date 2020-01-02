"""
  Create a function (or write a script in Shell) that
  takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""


def check_even_or_odd(input_number):
    if input_number % 2 != 0:
        return "Odd"
    return "Even"


def even_or_odd(number):
    return "Odd" if number % 2 != 0 else "Even"


print(check_even_or_odd(10))
print(check_even_or_odd(7))

print(even_or_odd(2) == "Even")
print(even_or_odd(0) == "Even")
print(even_or_odd(7) == "Odd")
print(even_or_odd(1) == "Odd")
print(even_or_odd(-1) == "Odd")
