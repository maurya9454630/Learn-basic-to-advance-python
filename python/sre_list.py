# list => mutable, ordered, value change, indexing, slising 
# a = [1,2,4,56,64,67,'saa',print()]
# print(a)
# print(a[::])

# first way using list
# a = [1,23,43,53,62,3.2,8]
# for i in range(len(a)):
#     print(a[i])

# second way access list

# a = [1,23,43,53,62,3.2,8]
# for i in a:
#     print(i)

# print positive and negative number in list 
# l = [1,2,4,5,6,-2,-5]
# print("positive value: ")
# for i in l:
#     if i >= 0:
#         print(i)
# print("neagative value: ")
# for i in l:
#     if i < 0:
#         print(i)

# mean of list element 
# l = [2,3,5,6,7,4,8]

# sum = 0
# for i in l:
#     sum = sum + i
# print(sum/len(l))

# find the greatest element and print the index too.

# l = [12,33,53,64,452,43,57]
# largest  = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i
# print(f"your largest number is {largest} at index {index}")

# find the second greatest element and print the index too.

# l = [2,54,6,34,78,35,90]
# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
# print(sec_largest,largest)


# check if list is sorted or not.

l = [12,4,67,86,43,7,98]
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
     print("your list is sorted")