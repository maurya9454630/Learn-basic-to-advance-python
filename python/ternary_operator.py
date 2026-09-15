# Single line ternary operator

food = input("food :")
eat = "Yes" if food == "cake" else "no"
print(eat)

# second step 

food = input("food :")
print("sweet") if food == "cake" or food == "khoa" else print("not sweet")

# clever if / Ternary Operator 

age = int(input("age : "))
vote = ("yes", "no")[age >= 18]
print(vote)



sal = float(input("salary : "))
tax = sal*(0.1,0.2) [sal<=50000]
print(tax)