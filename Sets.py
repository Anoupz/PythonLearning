"""
Learning of Sets
"""

fav_foods: set = {"blueberry", "grapes"}
print(fav_foods)

fav_foods.add("apple")
print(fav_foods)

fav_foods.add("apple")
print("this will not add as apple is present in the set", fav_foods)
fav_foods.remove("apple")
print(fav_foods)

# Integers from 1 to 10

odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}

print(odd.union(even))
print(odd.intersection(even))
print(3 in odd)

# Set comprehensions.

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]

my_set = {num for num in nums}
print("Set comprehensions. --->>>", my_set)
