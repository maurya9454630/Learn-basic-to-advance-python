# list, dictonary and set comprehension.
# list
l = [i for i in range(1,21) if i % 2 == 0]
print(l)

# dictonary

l = {i: i**2 for i in range(1,10)}
print(l)

# lambda function 

# add = lambda a,b : a + b
# print(add(12,12))

# addition = lambda a : "even" if a %2 == 0 else "add"
# print(addition(12))

# map 

a = [1,2,3,4,5]
result = map(lambda x : x*2,a)
print(result)

