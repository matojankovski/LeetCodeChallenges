def isAnagram( s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    d_s, d_t = {}, {}

    for i in range(len(s)):
        d_s[s[i]] = d_s.get(s[i], 0) + 1
        d_t[t[i]] = d_t.get(t[i], 0) + 1
    return d_s == d_t

def groupAnagrams(strs):
    anagram_dict = {}

    for i in strs:
        sorted_strs = sorted(strs)
        key = tuple(sorted_strs)

        if key not in anagram_dict:
            anagram_dict[key] = [i]
        else:
            anagram_dict[key].append(i)

    return anagram_dict.values()


    # AnagramsList = []
    # helpList = []
    # for i in range(0, len(strs)):
    #     for j in range(i+1, len(strs)):
    #         if isAnagram(strs[i], strs[j]):
    #             helpList.append(strs[i])
    #             helpList.append(strs[j])
    #     AnagramsList.append(helpList)
    #     helpList = []
    #
    # return AnagramsList

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))