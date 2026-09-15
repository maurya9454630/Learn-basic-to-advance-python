# WAP to check if a list contains a palindrome of elements. (Hint : use copy() method)

list = [1,2,3]
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrone")
else:
    print("not palindrone")

#WAP to count the number of students with the "A" grade in the following tuple.

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# WAP to create list & shot 

alp = ["a", "b", "d", "c", "e", "g", "f"]
alp.sort()
print(alp)