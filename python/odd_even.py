#WAP to check if a number entered by the user is odd or even.

num = int(input("Enter a number : "))
rem = num % 2
if(rem == 0):
    print("Even")
else:
    print("Odd") 

#WAP to find greatest of 3 number check largest number
a = int(input("Enetr a first number : "))
b = int(input("Enetr a second number : "))
c = int(input("Enetr a third number : "))

if(a >= b and a >=c):
    print("first number is largest: ",a)
elif(b >= c):
    print("second number largest : ",b)
else:
    print("third number largest : ",c)

# WAP to check if a number is a multiple of 7 or not.

x = int(input("Enter a number : "))

if(x % 7 == 0):
    print("multipal of 7 ")
else:
    print("not a multipal ")
