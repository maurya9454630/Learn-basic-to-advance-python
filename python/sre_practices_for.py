#accept an integer and print hello world n time.
# n = int(input("please tell your number: "))
# for i in range(n):
#     print("Hello World")

# print natural number up to n.
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(i)

# Reverse for loop print n to 1. 
# n = int(input("Enter a number: "))
# for i in range(n,0,-1):
#     print(i)


# take a number as input and print its table.

# n = int(input("Which table to want: "))
# for i  in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# Sum up to n term.

# n = int(input("please tell your number: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f"your sum is: {sum}")

# factorial number.

# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,1+n):
#     fact = fact * i
# print(f"your factorial value {fact}")

# print the sum of all even & odd numbers in a range separately.

# n = int(input("tell your number: "))
# even = 0
# odd = 0
# for i in range(1,10,2):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"your even and odd sum are {even}, {odd}")

# print all the factors 
# n = int(input("which number factors you want: "))

# for i in range(1, n+1):
#     if n%i == 0:
#         print(i)

# Accept a number and check if a perfect number or not.A number whose sum of factors is equal to the number itself. => ex- 6= 1,2,3 =6
# n = int(input("which number factors you want: "))
# sum = 0
# for i in range(1, n):
#     if n%i == 0:
#         sum = sum + i
# # print(f"the factors of sum {sum}")
# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")

# check weather the number is prime or not.
# n = int(input("Check your number is prime or not: "))
# count = 0
# for i in range(1, n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")

# Reverse a string without using in build function.

# a = "Rahan"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     # print(a[i])
#     b = b + a[i]
# print(b)

# check string is pallindrome or not.

# a = "naman"
# a = str(input("Enter your name: "))
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("your string is pallindrome")
# else:
#     print("your string is not pallindrome")

# counts all laters, digits and special symbols from a given string.

a = "dasws123@#$!%^^$"
char = 0
dig = 0
spchar = 0
for i in a:
    if i .isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        spchar += 1
print(f"your digits are {dig}\n your alphabets are {char}\n your spchar {spchar}")
        







