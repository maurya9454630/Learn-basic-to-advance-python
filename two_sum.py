#  Two Sum 

def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i

    return []

nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)
print(result)