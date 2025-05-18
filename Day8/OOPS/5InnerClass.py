class Student:
    def __init__(re,name,rollno):
        re.name=name
        re.rollno=rollno
        re.lap=re.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
        
    class Laptop:
        def __init__(self) : 
            self.brand='MSI'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student('SANKAR',23)
lap1=Student.Laptop()
s1.show()
            