from operator import attrgetter

nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]

sorted_nums = sorted(nums)

print("Sorted nums is", sorted_nums)
print(f"Original value is {nums}")

nums.sort()
print(f"InBuilt sort function updates the existing list, {nums}")


tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)

sorted_tup = sorted(tup)

print("Tuples don't have inbuilt sort function", sorted_tup)

num_li = [-5, -6, -4, 1, 2, 3]

sorted_num_li = sorted(num_li)

print(sorted_num_li)

print("To get the abs value based sorted function")
abs_sorted_num_li = sorted(num_li, key=abs)
print(abs_sorted_num_li)


# Sorting in classes can be done as follows


class Employee:
    def __init__(self, name, age, salary):
        super().__init__()
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name},{self.age},{self.salary}"


e1 = Employee("Carl", 59, 6000)
e2 = Employee("Jon", 39, 12000)
e3 = Employee("Max", 49, 8000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.salary


sorted_employees_by_lambda = sorted(employees, key=lambda e: e.age)
sorted_employees_by_fun = sorted(employees, key=e_sort, reverse=True)
sorted_employees_by_attrgetter = sorted(
    employees, key=attrgetter("name"), reverse=True
)

print(sorted_employees_by_lambda)
print(sorted_employees_by_fun)
print(sorted_employees_by_attrgetter)
