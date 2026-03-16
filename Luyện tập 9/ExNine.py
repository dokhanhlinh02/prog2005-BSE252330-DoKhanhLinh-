# Bài 9:
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Woof Woof!")
dog = Dog("Meo")
print("Dog name:", dog.name)
dog.sound()
