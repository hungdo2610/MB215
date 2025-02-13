class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year  # Public attribute for year

def compare_car_years(car1, car2):
    """Compares two Car objects based on their year."""
    if car1.year < car2.year:
        return f"{car1.make} {car1.model} ({car1.year}) is older than {car2.make} {car2.model} ({car2.year})"
    elif car1.year > car2.year:
        return f"{car2.make} {car2.model} ({car2.year}) is older than {car1.make} {car1.model} ({car1.year})"
    else:
        return f"Both cars are from the same year ({car1.year})"

# Instantiate two Car objects
car1 = Car("Toyota", "Camry", 2015)
car2 = Car("Honda", "Civic", 2018)

# Compare the cars
result = compare_car_years(car1, car2)
print(result)
