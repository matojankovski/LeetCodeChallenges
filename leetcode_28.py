def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    for i in range(len(haystack)+1-len(needle)):
        if haystack[i: i+ len(needle)] == needle:
            return i
    return -1


print(strStr("sadbutsad", "sad"))
print(strStr("hello", "ll"))
print(strStr("a", "a"))
print(strStr("abc", "c"))
print(strStr("aaa", "aaa"))
print(strStr("mississippi", "a"))
