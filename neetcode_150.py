def hasDuplicate(nums) -> bool:
    dict = {}
    for i, n in enumerate(sorted(nums)):
        dict[n] = dict.get(n,0) +1
        if dict[n] >= 2:
            return print('true')
        else:
            return print('false')

nums = [1,2,3,3]
hasDuplicate(nums)