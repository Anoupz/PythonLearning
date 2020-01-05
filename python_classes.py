import datetime


class Cars:
    runs = True

    def __init__(self, name):
        self.name = name

    def start(self):
        if self.runs:
            print(f"{self.name} car is runs started")
        else:
            print(f"{self.name} Car is broken :(")


class Vehicle:
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_fuel_efficient(self):
        if self.fuel == "gas":
            return True
        else:
            return False


# bmw = Cars("BMW")
# bmw.start()
#
# bmw.runs = False
# bmw.start()
#
# audi = Cars("Audi")
# audi.start()
#
# print(isinstance(bmw, Cars))


class Employee:
    # Class variables
    num_of_emp = 0
    raise_pay = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@test.com"
        Employee.num_of_emp += 1

    def apply_raise(self):
        return self.pay * self.raise_pay

    def full_name(self):
        return f"{first}{last}"

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_pay = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("Test", "User", 5000)
emp2 = Employee(last="Test2", first="User2", pay=9000)

emp3 = Employee.from_string("Test3-User3-10000")

print(emp1.first, emp1.apply_raise())
print(emp2.first, emp2.apply_raise())
print(emp1.num_of_emp)
print(emp3.email)

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
