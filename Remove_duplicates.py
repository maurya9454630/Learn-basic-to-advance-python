# Remove duplicate value. 

arr = [1, 2, 2, 3, 4, 4, 5]

new_arr = []

for num in arr:
    if num not in new_arr:
        new_arr.append(num)

print(new_arr)