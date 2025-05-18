class Engine:
    def __init__(self, power):
        self.power = power
    def start(self):
        return f"Engine with {self.power} power is starting."
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  
    def drive(self):
        return f"{self.brand} car is driving with {self.engine.start()}"
# Creating Engine object
engine1 = Engine("150 HP")
# Creating Car object with Engine object
car1 = Car("Toyota", engine1)
# Accessing both car and engine methods
print(car1.drive())
