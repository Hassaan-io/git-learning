class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"I\'m {self.name}, and I\'m {self.age} years old")
class Dog(Animal):
    def speak(self):
        print("Woof")
class Cat(Animal):
    def speak(self):
        print("Meow")
dog = Dog("Max","6")
cat = Cat("Luna", "2")
animals = [dog,cat]
for animal in animals:
    animal.introduce()
    animal.speak()