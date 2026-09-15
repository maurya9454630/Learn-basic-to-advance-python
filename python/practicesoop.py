# create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        pass

    # static method 
    @staticmethod  # decorator 
    def collage():
        print("ABC Collage")

    def get_avg(self):
        total  = 0
        for val in self.marks:
            total += val
        print("hi",self.name,"your avg score is:",total/len(self.marks))

s1 = Student("Tony stark",[87,76,98])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()
s1.collage()