# Classes
"""class Dog:
    def __init__(self, name, age):# type of constructor
        self.name = name
        self.age = age
    def bark(self): # whenever create a new object in a class need to point to that object use self
        print("I am a dog")
roger = Dog("Roger", 20)# we have created a dog name roger
print(roger.age)
print(roger.bark())# here it also give None as print is already inside bark function , so calling again print results in None
print(type(roger))"""
#inheritance
class Animal:# parent
    def walk(self):
        print("Walking.....")
class Dog(Animal):# child
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")
roger = Dog("Roger", 20)
print(roger.age)
roger.bark()
roger.walk()
