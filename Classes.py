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
