# Find missing number

arr = [1, 2, 3, 5]

n = 5

total = n * (n + 1) // 2

actual_sum = sum(arr)

missing = total - actual_sum

print("Missing number:", missing)