class Car():
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    # __str__() is meant for user-friendly output
    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}"
    
    # __repr__() is meant for a more detailed, unambigous output (representation method -> for debugging)
    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"
    
if __name__ == "__main__":
    car = Car("Toyota", "Yaris", 2007)

    # Using __str__(), user-friendly output: Toyota, Yaris, 2007
    print(str(car))
    # Using __repr__(), developer-friendly output: Car(make='Toyota', model='Yaris', year=2007)
    print(repr(car))