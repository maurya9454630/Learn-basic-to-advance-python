# oops concept of python programming.

# class Factory:
#     a = 12 #attribute

#     def hello(self): #method
#         print("How are you?")

# #     print("Hello how are you I am getting interast.")

# # print(Factory().a)
# # Factory().hello()

# obj = Factory()
# print(obj.a) 
# obj.hello()

# constructer 

# class Factory:
#     def __init__(self,material,zip,packet):
#         # print(self)
#         self.material = material
#         self.zip = zip
#         self.packet = packet

#     def show(self):
#         print(f"your object details are {self.material},{self.zip},{self.packet}") 

# reebok = Factory("leather",3,2)
# campus = Factory("naylon",3,3) 
# reebok.show()
# # print(reebok.material)

# attribute and methods

# class Animal:
#     name = "lion"  # class attribute

#     def __init__(self, age):
#         self.age = age  # instance attribute

#     def show(self):  # instance method
#         print(f"How are you age is {self.age}")

#     @classmethod
#     def hello(cls):
#         print("How are you brother")

#     @staticmethod
#     def static():
#         print("How are you")


# obj = Animal(12)

# obj.static ()

# inheritance class

# class Factorymumbai: #parent class / superclass
#     a = ("I am attribute mentioned inside factory")
#     def hello(self):
#         print("I am method mentioned inside factory")

# class Factorypune(Factorymumbai):#child class / subclass
#     pass
# obj = Factorymumbai()
# obj2 = Factorypune()
# print(obj2.hello())

# Constructor in Inheritance 

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(f"Hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         print(f"Hello your name is {self.name},{self.age}")#method overrading.


# animal1 = Animal("Lion")
# person1 = Human("akasher",23)
# person1.show()

# harercy

# class Animal:
#     name1 = "Lion"

# class Human:
#     name2 = "Harsh"

# class Robots(Animal,Human):
#     name3 = "aman123"

# obj = Robots()
# print(obj.name3)

#  multilevel inheritance

# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips

# class BhopalFactory:
#     def __init__(self,material,zips,color):
#         super().__init__(material,zips)
#         self.color = color

# class PuneFactory:
#     def __init__(self,material,zips,color,pockets):
#         super().__init__(material,zips,color)
#         self.pockets = pockets

# Polymorphism =>method override

# class Animal:
#     def show(self):
#         print("Hello i am lion")
 
# class Human(Animal):
#     def show(self):
#         print("How are you")

# obj = Human()
# obj.show()

# duck type

# class Animal:
#     def show(self):
#         print("I am showing animal")

# class Human:
#     def show(self):
#         print("I am showing human")

# obj1 = Animal()
# obj2 = Human()
# obj1.show()
# obj2.show()

#  Encapsulation =>public,protected
# private me attribut define karte vakt double undescore,def show(__) is private value no access other value.


# class Factory:
#     __a = "pune"

#     def __show(self):
#         print("Hello i am a pune factory") 

# class Bhopal(Factory):
#     def show2(self):
#         print(super().__a)

# obj = Bhopal()
# obj.show2()
  
# private access
# class Factory:
#     __a = "pune"

#     def show(self):
#         print(Factory.__a)

# obj = Factory()
# obj.show()

# Abstraction

# from abc import ABC, abstractmethod

# class Abstract(ABC):

#     @abstractmethod
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass

# class Square(Abstract):

#     def __init__(self, side):
#         self.side = side

#     def perimeter(self):
#         print("Square perimeter =", 4 * self.side)

#     def area(self):
#         print("Square area =", self.side * self.side)

# class Circle(Abstract):

#     def __init__(self, radius):
#         self.radius = radius

#     def perimeter(self):
#         print("Circle perimeter =", 2 * 3.14 * self.radius)

#     def area(self):
#         print("Circle area =", 3.14 * self.radius * self.radius)

# obj = Circle(7)
# obj2 = Square(12)

# obj.perimeter()
# obj.area()

# obj2.perimeter()
# obj2.area()

#  dunder method 

# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return(f"Hello how are you and your name is {self.name}")

#     def __add__(self, other):
#         return(f"your sum of age {self.age + other.age}")

# obj = Animal("Lion",12)       
# obj2 = Animal("dolphin",14)
# print(obj + obj2)

# decorater in python

class Animal: 
    @property
    def show(self):
        print("Hello how are you?")

obj = Animal()
obj.show

