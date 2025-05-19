class MyClass:
    class_variable = 10
    def static_method(x, y):
        return x + y
    def class_method(cls, increment):
        cls.class_variable += increment  
class SecondClass(MyClass):
    def static_method(x, y):
        return x + y
    
    def class_method(cls, increment):
        cls.class_variable += increment 
obj1=SecondClass()
print(obj1.class_variable)
                      
