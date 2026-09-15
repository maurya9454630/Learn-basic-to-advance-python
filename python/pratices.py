# store following word meanings in a python dictionary

dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "List of fact & figures"]

}
print(dict)

# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classroom are needed by all students.

subjects = {
    "Python", "Java", "C++", "Python", "javascript", "Java",
    "Python", "Java", "C++","c"
}
print(subjects)
print(len(subjects))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start a empty dictionary & add one by one. Use subject name as key & marks as a value.
marks = {}
x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter che : "))
marks.update({"che" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

print(marks)

# Figure out a way to store 9 & 9.0 as separate value in the set.(You can take help of built-in data types).

values = {9,9.0}
print(values)