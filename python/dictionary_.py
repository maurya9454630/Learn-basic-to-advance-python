# WAP Dictionary key-value in pair.

dict = {
    "name" : "Mohan",
    "cgpa" : 8.9,
    "marks" : [88, 95,70]
}
print(dict)# key-value print 
print(dict["name"])# value print
print(dict["marks"])# value print
print(type(dict))

# Nested dictionary

student = {
    "name" : "Rohan",
    "subject" : {
    "python" :  89,
    "java" : 88,
    "PHP" : 99,
    }

} 
print(student)#dictionary 
print(student["subject"])
print(len(list(student.keys())))
print(list(student.items())) #return all(key, value)pairs as tuple 
pairs = list(student.items())
print(pairs[0])

print(student["name"])
print(student.get("name")) # return the key according to value

student.update({"city" : "delhi"}) # inserts the specified items to the dictionary 
print(student)

