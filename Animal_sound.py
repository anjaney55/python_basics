class Animal:
    def __init__(self,name):
        self.name =name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow!"
    
dog = Dog("Buddy")
print(dog.make_sound()) # Buddy says Woof!

# Dog.make_sound(dog) # Buddy says Woof!
