# Accept two numbers and print the grestest between them.

# num1 = int(input("Enter a first number: "))
# num2 = int(input("Enter a Second number: "))

# if num1 > num2:
#     print(f"{num1} is greater then {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater then {num2}")    
# else:
#     print("Both the numbers are same.")

#  Accept the gender from the user as char and print the respective greeting message 

# gen = input("please tell your gender as character (M or F):- ")

# if gen == 'M' or gen == 'm':
#     print("Good morning Sir.")
# elif gen == 'F' or gen == 'f':
#     print("Good morning ma'm")
# else: 
#     print("Unidentified gender")

# Accept an integer and check weather it is an even number or odd.

# a = int(input("Enter a number: "))
# if (a % 2) == 0:
#     print("Even Number")
# else: 
#     print("Odd Number")


# Accept name and age from the user. Check if the user is a valid voter or not.

# vote = int(input("Enter a number: "))

# if vote >= 18:
#     print("hello harsh valid voter")
# else:
#     print("hello harsh not valid voter")

# accept a year and check if it a leap year or not 

# year = int(input("tell your year: "))
# if year %100 == 0 and year %400 == 0:
#     print("Its a leap year")
# elif year %100 != 0 and year %4 == 0:
#     print("Its a leap year")
# else:
#     print("Its a normal yera")

# tempracher 

t = int(input("please tell the temprature :- "))
if t < 0:
    print("Freezing cold")

elif t >= 0 and t < 10:
    print("very cold")

elif t >= 10 and t < 20:
    print("cold")

elif t >= 20 and t < 30:
    print("plesant")

elif t >= 30 and t < 40:
    print("hot")
else:
    print("very hot")
