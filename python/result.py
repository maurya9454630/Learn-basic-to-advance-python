marks = int(input("Enter a student marks : "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"    
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the student -> ", grade)

#age of nesting condition

age = 95

if(age >= 18):
    if(age >= 80):
        print("cannot drive.")
    else:
        print("can drive.")
else:
    print("cannot drive.")