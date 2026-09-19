# tuple =>immutable, dublicate, parathesis brecket, no change value,

# a = (2,3,4,6,5)
# print(type(a))

# first way access tupple
# for i in a:
#     print(i)

# second way access tuple
# for i in range(len(a)):
#     print(i)

# a = (2,4,5,7,3,7,3)
# index = a.index(3)
# print(index)

# a = (2,4,5,7,3,7,3)
# count = a.count(3)
# print(count)

# a = (1,)
# print(type(a))
# ===================================================================================
# set => no dublicate value, mutable value change,

# set = {3,5,7,4,3,0}
# print(type(set))

# hash = hash("Hello")
# print(hash)

# a = {2,4,5,7,"hello",8,9,0}
# for i in a:
#     print(i)

# a = {2,3,5,7,4,8,0,9}
# # a.remove(2)
# a.pop()
# print(a)

# union part
# a = {1,2,3,4,5}
# b = {6,7,8,9,0,2,3,4}
# s = a.union(b) #s = a | b
# print(s)

# intersection
# a = {1,2,3,4,5}
# b = {6,7,8,9,0,2,3,4}
# s = a.intersection(b) #s = a & b
# print(s)

# difference 
# a = {1,2,3,4,5}
# b = {6,7,8,9,0,2,3,4}
# s = b.difference(a) #s = b - a
# print(s)

# symmetric difference 

# a = {1,2,3,4,5}
# b = {6,7,8,9,0,2,3,4}
# s = a.symmetric_difference(b) #s = a ^ b
# print(s)
# =======================================================================================

# dictionary => curly brecket, mutable, dublicate value no key vale allow, 

# d = {1:"hello",2:23}
# d[1] = 10 #creating 
# d[3] = 30 #updating
# print(d)
 
# d = {1:10,2:20,3:30,4:40,5:50}
# for i in d:

#     print(d[i])

# help(dict)

# d ={11:100,12:200,13:300}
# print(d.items())

# write a python script to manage two python dictonary.

# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}

# for i in d2: 
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]


