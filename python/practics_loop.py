# print numbers from 1 to 100
# jo variabl hota hai use itrater kahte hai. jitni bar loop count hota itration kahte hai.
i = 1
while i <=100:
    print(i)
    i +=1
    print("Second program")

# print numbers from 100 to 1.
j = 100
while j >= 1:
    print(j)
    j -=1

# print the multiplication table of a number n.

n = int(input("Enter number : "))
a = 1
while a <=10:
    print(n*a)
    a +=1

# print the elements of the following list using a loop. 

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1

# Search for a number x in this tuple using loop.

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
b = 0
while b < len(nums):
    if(nums[b] == x):
        print("Found index : ",b)
    else:
        print("finding...")
    # print(nums[b])
    b += 1

    