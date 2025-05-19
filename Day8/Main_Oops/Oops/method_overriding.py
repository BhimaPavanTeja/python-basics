class Parent:
    def show(self):
        print("Parent Class")
class Child(Parent):
    def show(self):
        print("Child Class")
class GChild(Child):
    def show(self):
        print("GChild Class")
obj = GChild()
obj.show()