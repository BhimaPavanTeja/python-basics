class Example:
    def add(self, a=0, b=0, c=0):
        if(a!=0 and b!=0 and c!=0):
            return a+b+c
        elif(a!=0 and b!=0 and c==0):
            return a+b
        else:
            return a
    
obj1 = Example()
obj2= Example()
print(obj1 is obj2) 

 