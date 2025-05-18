class Hello:
    # default constructor
    def __init__(self):
        print( "I'm from Default Constructor")
    # a method for printing data members
    def print_image(self):
        pass
# creating object of the class
obj1 = Hello()
obj2 = Hello()
# calling the instance method using the object obj
obj1.print_image()
obj2.print_image()
