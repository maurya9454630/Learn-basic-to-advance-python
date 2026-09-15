# Write a recursive function to calculate the sum of first n natural numbers.

def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(5)
print(sum)

# Write a recursive function to print all elements in a list. 
# Hint : use list & index as parameters.

def print_list (list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango", "banana", "apple", "lichi"]
print_list(fruits)

