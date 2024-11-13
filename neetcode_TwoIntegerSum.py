def twoSum(nums, target):
    hashmap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i

nums = [3,4,5,6]
target = 7
print(twoSum(nums, target))
nums = [4,5,6]
target = 10
print(twoSum(nums, target))
