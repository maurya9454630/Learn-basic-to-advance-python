# metod 
class Student:
    def __init__(self,marks):
        self.marks = marks
        # pass

    def welcome(self):
        print("Welcome Student")

    def get_marks(self):
        return self.marks

s1 = Student(48)
s1.welcome()
print(s1.get_marks())

