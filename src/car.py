class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"make: {self.make}, model: {self.model}, year: {self.year}"

if __name__ == "__main__":
    car1 = Car("Toyota","Rav4", 2020)
    print(car1)