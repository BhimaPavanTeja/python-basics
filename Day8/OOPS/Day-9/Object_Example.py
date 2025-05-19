class Dog:
    greetings = "welcome"

    def bark(self, name):
        print(f"Hello {name}!")

# Object for class Dog
dog1 = Dog()
print(dog1.greetings)
dog1.bark("Buddy")
