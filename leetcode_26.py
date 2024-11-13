nums = [1,1,2]
nums1 = [0,0,1,1,1,2,2,3,3,4]
nums2 = [-1,0,0,0,0,3,3]
def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

def

print(removeDuplicates(nums))
print(removeDuplicates(nums1))
print(removeDuplicates(nums2))