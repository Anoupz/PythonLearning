from python_classes import Vehicle, Employee


class Honda(Vehicle):
    def __init__(self, make, model, num_wheels=4):
        super().__init__(make, model)
        self.number_of_wheels = num_wheels

    def start(self):
        print(
            f"You have {self.make} {self.model} car which run on {self.fuel} and has {self.number_of_wheels} wheels"
        )


my_honda = Honda("Honda", "CRV")
my_honda.start()
print("Is My car fuel efficient ?? ", my_honda.is_fuel_efficient())


class Truck(Vehicle):
    number_of_wheels = 6

    def __init__(self, make, model, fuel):
        super().__init__(make, model, fuel)

    @property
    def make_model(self):
        return f"Make is {self.make} and model is {self.model}"

    @make_model.setter
    def make_model(self, name):
        make, model = name.split("-")
        self.make = make
        self.model = model

    def start(self):
        print(
            f"You have {self.make} {self.model} which run on {self.fuel} and has {self.number_of_wheels} wheels"
        )


large_truck = Truck(make="Tesla", model="Cyber", fuel="Diesel")
large_truck.start()
print("Is my truck fuel efficient ?? ", large_truck.is_fuel_efficient())
large_truck.make_model = "Honda-CRV"
print(large_truck.make_model)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev_1 = Developer("Test4", "User4", 90090, "Python")
print(dev_1.email)
print(dev_1.prog_lang)
