# A perfect number is a number whose proper divisors add up to the number itself

num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is Not a Perfect Number")