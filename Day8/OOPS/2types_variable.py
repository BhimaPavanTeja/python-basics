class car:
    wheels=4
    def __init__(self):
        self.brand='bmw'
        self.milega=10
c1=car()
c2=car()
c2.brand='swift'
print(c1.brand,c1.milega,c1.wheels)
print(c2.brand,c2.milega,c2.wheels)
c1.wheels=2
print(c1.brand,c1.milega,c1.wheels)
print(c2.brand,c2.milega,c2.wheels)       
    