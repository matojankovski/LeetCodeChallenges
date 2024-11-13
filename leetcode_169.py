nums1 = [3,2,3]
nums2 = [2,2,1,1,1,2,2,8,8,8,8]
nums4 = [3,3,4]
d_n1 = {}
most_freq_element = None

def find_the_most_occured(nums):
    map = {}
    maxCount, res = 0, 0
    for n in (nums):
        map[n] = map.get(n,0) +1
        if map[n] > maxCount:
            res = n
        maxCount = max(map[n], maxCount)
    return res

print(find_the_most_occured(nums1))
print(find_the_most_occured(nums2))
print(find_the_most_occured(nums4))


