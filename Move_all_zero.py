#  Move all zeros to the end

def move_zeros(arr):
    non_zero = []

    for num in arr:
        if num != 0:
            non_zero.append(num)

    zero_count = len(arr) - len(non_zero)

    return non_zero + [0] * zero_count


arr = [0, 1, 0, 3, 12]

result = move_zeros(arr)

print(result)
