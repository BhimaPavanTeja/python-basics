class student:
    school_Name="SVB"
    def __init__(self,m1,m2,m3) :
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)//3
    @classmethod
    def getSchool(cls):
        return cls.school_Name
    @staticmethod
    def info():
        print("this is a static method")
s1=student(12,23,44)
print("Student1_Mark : ",s1.avg())
s2=student(72,83,94)
print("Student2_Mark : ",s2.avg())
print(student.getSchool())
student.info()

        