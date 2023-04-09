class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, num_of_doors, type_of_roof):
        super().__init__(vehicle_type)
        self.vehicle_type = vehicle_type
        self.year = year
        self.make = make
        self.model = model
        self.num_of_doors = num_of_doors
        self.type_of_roof = type_of_roof

vehicle_type = "car"
year = input("What year was the automobile made?:\n")
make = input("What is the make of the automobile?:\n")
model = input("What is the model of the automobile?:\n")
num_of_doors = input("Does the automobile have 2 or 4 doors?:\n")
type_of_roof = input("Does the automobile have a solid or sun roof?:\n")

car = Automobile(vehicle_type, year, make, model, num_of_doors, type_of_roof)

print(f"Vehicle type: {car.vehicle_type}")
print(f"Year: {car.year}")
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Number of doors: {car.num_of_doors}")
print(f"Type of roof: {car.type_of_roof}")