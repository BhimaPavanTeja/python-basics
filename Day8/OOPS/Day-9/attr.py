class Dog:
    species = "Canine"  
    # Class attribute
    def __init__(self, name):
        self.name = name  
	 # Instance attribute
dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(f"dog1 speciesc is {dog1.species} and the name is : {dog1.name}")
print(f"dog2 speciesc is {dog2.species} and the name is : {dog2.name}")


