# WAP to print the length of a list.(list is a parameter).

citys = ["delhi", "mumbai", "lucknow", "noida", "pune", "chennai"]

def print_len(list):
    print(list)
    # return list
print_len(citys)

# WAF to print the elements of a list in a single line.(list is the parameter)

heroes = ["thor", "ironman", "caption america", "shaktiman"]

def print_list(lists):
    for item in lists:
        print(item,end=" ")
print_list(heroes)

# WAF to find the factorial of n. (n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)

cal_fact(5)

# WAP to convert USD to INR. 

def converter (usd_val):
    inr_val = usd_val *90
    print(usd_val,"USD = ",inr_val,"INR")
converter(1)


# Recursion function.

def show(n):
    if (n == 0):
        return  
    print(n)
    show(n-1)
show(5)

# recursion factorial

def fact1(n):
    if(n == 1 or n == 0):
        return 1
    return fact1(n-1)*n

print(fact1(3))
