class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def myfunc(p1):
        print("Hello my name is " + p1.name)
p1 = Person("Murali",36)
p1.myfunc()
