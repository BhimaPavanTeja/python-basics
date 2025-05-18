class Mobile:
    def __init__(self, brand, model, storage=128):
        self.brand = brand
        self.model = model
        self.storage = storage
  
    def config(self):
        print(f"Mobile Config - Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")
        
mob1 = Mobile("Samsung", "Galaxy S21")
mob2 = Mobile("Apple", "iPhone 14", 256)

mob1.config()
mob2.config()
