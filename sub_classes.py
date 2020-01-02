from Classes import Vehicle


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
