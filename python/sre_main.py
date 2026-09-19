# print("Namaste python.")

# Seryansschool = "harsh " #pascal case
# SeryansSchool = "harsh " #camel case
# seryans_school = "harsh " #snake case


# data type => int ,float, complex, string, boolean.

# a = 33

# b = 98.9
# c = 12/3

# v = 34j
# print(type(v))

# st = '23134 degree !3#@'

# print(type(st))

# b = True
# t = False

# print(type(b))

# a = "A"
# print(ord(a)) # unic code converter => ord

# a = 65
# print(chr(a)) # convert of char

#string indexing access a value.

# a = "Harsh"
# # print(a[0:3])
# print(a[-1],a[4])

# sclicing value 

# a = "Aman Coder"
# print(a[0:3:1])
# print(a[5::1])

# type conversion 

# a = 12
# a = str(a)
# print(type(a))

# input and output 

# formated string 
# name = "Aman"
# age = 24

# print("Hello my name is ",name," and my age is ",age,"")
# print(f"my name is {name} and my age is{age}")

# a = int(input("Enter my age: "))
# print("my age",a)

# arithmetic operation

# a = 30
# b = 10

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(b**2)
# print(12+4/2)

# assigment operators 
# a = 23

# compound assignment operations 

# a = 20
# a = a + 20
# a += 20
# a -= 10
# a *= 5
# a /= 2
# a //= 2
# a **= 2

# print(a)

# comparison Operator 

# a = 12
# b = 12

# print(a == b)

# print(a != b)

# print(a > b)
# print(23 < 45)
# print(23 >= 22)
# print(23 <= 24)

# print(ord("a"))
# print(ord("b"))
# print("a" < "b")
# print(chr(89))

# logical operators => and=all true, or=any one true, not
# print(12 > 20 and 123 > 100 and 34 == 34 and 45 < 90)
# print(12 != 12 or 23 == 45 or 10 > 5)

# type of conditional Statements 
# if else 
# a = 13
# if a > 10:
#     print("I will do task A")
# else: 
#     print("I will do task B")


# money = int(input("please provide me the money: "))
# if money == 10:
#     print("I will have a choco bar icecream")
# elif money == 20:
#     print("I will have a mango dolly")
# else:
#     print("I will have a cone")

# there are two type=> loop for loop, while loop

# for loop
# a = range(1,20,1)
# for i in range(2,21,2):
#     print(i)
  
# a = "Harsh"
# print(len(a))
# for i in range(len(a)):
#     print(a[i])

# for i in range(1,21):
#     if i == 15:
#         break
#     else:
#         print(i)

# for i in range(1,21):
#     if i == 15:
#         continue
#     else:
#         print(i)

# while loop 

# a = 1
# while a <= 30:
#     print(a)
#     a = a + 1

# Separate each digit of a number and print it on the new line.

# a = int(input("Tell your number: "))
# while a > 0:
#     print(a % 10)
#     a = a//10

# Accept a number and print is reverse.

# a = int(input("Enter a number: "))
# rew = 0
# while a > 0:
#     rew = rew * 10 + a % 10
#     a = a // 10
# print(rew) 

# palindrome number

# a = int(input("Enter a value: "))
# copy = a
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a//10
# if copy == rev:
#     print("pallindrome number")
# else:
#     print("not pallindrome number")
 
# random number generator

# import random 
# num = random.randint(1,11)
# # print(num)
# tries = 0

# while True:
#     guess = int(input("please guess your number 1 to 10: "))

#     if num == guess:
#         tries += 1
#         print(f"you are right you guessed the number is {tries} tries")
#         break

#     elif num < guess:
#         print("go a little lower")
#         tries += 1

#     elif num > guess:
#         print("go a little higher")
#         tries += 1

#     else:
#         tries += 1
#         print("sorry you are wrong") 


#  exception error

# a = int(input("Tell your number: "))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"Sorry there is an err as {err}")
# else:
#     print("good there is no exception")
# finally:
#     print("I will run no matter what")  

# print("ok i have done the division")

# raise error

# age = int(input("enter your age: "))
# try:
#     if age < 10 or age > 18:
#       raise ValueError("your age must be betwee 10 and 18")
#     else:
#       print("welcome to the club")
# except Exception as err:
#    print(f"an error accured as {err}")
# print("the club will start soon")

# file handling

# p = open("javascript/list.py")
# p = open('javascript/main.py')
# print(p.read())

# r = open("superman.txt",'w')
# r = open("raju.txt",'x')

# r.write("and now I am appending some content inside the file.")
# r.close()





