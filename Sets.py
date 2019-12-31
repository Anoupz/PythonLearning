"""
Learning of Sets
"""

fav_foods: set = {"blueberry", "grapes"}
print(fav_foods)

fav_foods.add("apple")
print(fav_foods)

fav_foods.add('apple')
print("this will not add as apple is present in the set", fav_foods)
fav_foods.remove('apple')
print(fav_foods)

# Integers from 1 to 10

odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}

print(odd.union(even))
print(odd.intersection(even))
print(3 in odd)
