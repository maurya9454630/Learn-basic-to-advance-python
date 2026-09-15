# print numbers from 1 to 100.

for i in range(1,101):
    print(i)

# print numbers from 100 to 1.

for j in range(100, 0, -1):
    print(j)

# print the multiplication table of a number n.

n = int(input("Enter a number : "))
for x in range(1, 11):
    print(n*x) 

# pass statement => ka matalb loop ko likhana par koi kam mat lena .

for a in range(3):
    pass      
print("Some useful work.")