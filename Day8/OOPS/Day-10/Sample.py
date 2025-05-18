class Parent1:
    def assetGF(self):
        print("One Million Rupees ")
class Parent2:
    def assetF(self):
        print("Two Million Rupees")
class Son(Parent1,Parent2):
    def assetSon(self):
        print("Empty Pocket")
f1=Son()
f1.assetF()
f1.assetGF()
f1.assetSon()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# class Son(Father):
#     def assetSon(self):
#         print("Empty Pocket")
# child=Son()
# child.assetGF()
# child.assetF()
# child.assetSon()