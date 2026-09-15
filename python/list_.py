# string==> inmutable change nahi kiya ja sakta hai
# list => mutable change kiya ja sakata hai.
# list marks

marks = [45,77,89,54,76,98,66,54]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0:])
print(marks[:2])
print(marks[-3:-1])

# student list

student = ["ram", 95.4, "Delhi"]
print(student)
student[0] = "Ramesh"
print(student)