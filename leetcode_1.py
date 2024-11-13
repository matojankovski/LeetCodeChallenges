def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            two_sums = nums[i] + nums[j]
            if two_sums == target:
                return [i, j]

def twoSumsHash(nums, target):
    map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in map:
            return [map[diff], i]
        map[n]=i

def create_hash(num):
    map = {}
    for i, n in enumerate(sorted(nums)):
        map[n]=i
        if n in map:
            map[n] +=1
    print(map)



nums = [2,7,19,15]
target = 9
create_hash(nums)

print(twoSum(nums, target))
print(twoSumsHash(nums, target))

nums = [3,2,4]
target = 6
print(twoSum(nums, target))
print(twoSumsHash(nums, target))

nums = [3,3]
target = 6
print(twoSum(nums, target))
print(twoSumsHash(nums, target))




