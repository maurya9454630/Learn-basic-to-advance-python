# for loop

num = [1,3,4,6,7,4,8]
for val in num:
    print(val)

str = "apnacollage"
for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)

# print the elements of the following list using a loop.

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)

# Search for a number x in this tuple using loop. 

a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)

x = 49
ind = 0 
for ele in a:
    if(ele == x):
        print("number found of ind ", ind)
    ind += 1