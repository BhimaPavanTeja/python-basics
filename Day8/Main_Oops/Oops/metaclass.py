class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['class_name'] = name
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.class_name)



from datetime import datetime

class TimestampMeta(type):
    def __new__(cls, name, bases, dct):
        dct['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=TimestampMeta):
    pass

class AnotherClass(metaclass=TimestampMeta):
    pass

print(MyClass.created_at)  
print(AnotherClass.created_at)  
