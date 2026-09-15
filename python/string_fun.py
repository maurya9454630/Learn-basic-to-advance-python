str = "I am studying python from home."
print(str.endswith("home")) #returns true if string ends with substr
print(str.capitalize()) #capitalizes 1st char
print(str.replace("home","collage")) #replaces all occurrences of old
print(str.find("am"))#return 1st index of 1st occurrer
print(str.count("studying")) # counts the occurrence of substr

# WAP to input user's first name & print its length.

name = input("enter a name : ")
print(name)
print("lenght of name : ",len(name))

#WAP to find the occurrence of '$' in a string.

str1 = "hi, $Iam the $ symbol $99.99."
print(str1.count("$"))
