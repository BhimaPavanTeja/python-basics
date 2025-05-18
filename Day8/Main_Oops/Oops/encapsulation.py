class Car:
    def __init__(self, speed):
        self._speed = speed  

    def set_speed(self, speed):
        if speed > 0:
            self._speed = speed

    def get_speed(self):
        return self._speed

car = Car(100)
car.set_speed(150)
print(car.get_speed())  
print(car._speed)