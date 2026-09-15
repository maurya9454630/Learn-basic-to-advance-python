# WAP to find the factorial of first n numbers, (using for).

n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial : ",fact) 

a = int(input("Enter a number : "))
fact_ = 1
for j in range(1, a+1):
    fact_ *= j
print("Factorial : ",fact_)