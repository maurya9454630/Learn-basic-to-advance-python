# OOP program. 
class Student:

#default constructors 
    def __init__(self):
        pass
    
    #paramitrize constructors 
    def __init__(self, name,marks): #costructer in python
        #print(self)
        self.name = name
        self.marks = marks
        print("Adding new student in database...")

s1 = Student("Karan",89)
print(s1.name,s1.marks)

s2 = Student("Ram",98)
print(s2.name,s2.marks)


# class Car():
#     color = "Blue"

# car1 = Car()
# print(car1.color)
