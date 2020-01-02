"""
  List Comprehensions
"""
NAMES = ["Anoop", "Akila", "Aditi"]

print([person for person in NAMES])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [n for n in nums]

print(my_list)

my_list = [n * n for n in nums]
print(my_list)

# Don't use lambda and with map as they are not readable and its always better to convert to comprehensions.
my_list = map(lambda n: n * n, nums)
print("Using Map and Lambda", my_list)

my_list = filter(lambda n: n % 2 == 0, nums)
print("Using Filter and Lambda", my_list)

my_list = [n for n in nums if n % 2 == 0]
print(f"Print all even numbers from my list --> {my_list}")

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print(
    "I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'",
    my_list,
)
