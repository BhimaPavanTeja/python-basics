class Father:
    def __init__(self):
        self.name="sankar"
        
    def show1(self):
        print("Parent1")

class Mother:
    def show2(self):
        print("Parent2")

class Child(Father, Mother):
    def show3(self):
        print(self.name)
        return self.show1()

obj = Child() 
obj.show3()  