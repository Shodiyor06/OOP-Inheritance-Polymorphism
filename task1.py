class Animal:
    def speak(self):
        return "animal voic"

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print("Dog:", dog.speak())
print("Cat:", cat.speak())
