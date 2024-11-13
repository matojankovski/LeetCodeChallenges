nums1 = [2,2,1]
nums2 = [4,1,2,1,2]
nums3 = [1]

def find_the_single_element(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(find_the_single_element(nums1))
print(find_the_single_element(nums2))
print(find_the_single_element(nums3))