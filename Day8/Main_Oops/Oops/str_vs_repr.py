class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'
    def __repr__(self):
        return f'Person({self.name}, {self.age})'
p = Person("Sankar", 24)
print(str(p))   
print(repr(p))  

import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))
