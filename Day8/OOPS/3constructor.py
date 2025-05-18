class Student:
    def __init__(self):
        self.name='Sankar'
        self.age=24
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False 
s1=Student()
s2=Student()
s2.age=25
if s1.compare(s2):
    print("they are same age")
else:
    print("They are not same age")
        