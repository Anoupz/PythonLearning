names = ["Peter Parker", "Clark Kent", "Wade Wilson"]
heros = ["Spiderman", "Superman", "Deadpool"]
universes = ["Marvel", "DC", "Marvel"]

for name, hero, universe in zip(names, heros, universes):
    print(f"{name} is actually {hero} from {universe}")

# You can unpack the same using zip function
for value in zip(names, heros, universes):
    print(value)  # this prints in tuple format


# Dictionary comprehensions.

my_dict = {name: hero for name, hero in zip(names, heros)}
print("Dictionary comprehensions.", my_dict)
