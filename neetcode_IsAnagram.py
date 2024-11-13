def isAnagram( s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    d_s, d_t = {}, {}

    for i in range(len(s)):
        d_s[s[i]] = d_s.get(s[i], 0) + 1
        d_t[t[i]] = d_t.get(t[i], 0) + 1
    return d_s == d_t

s = "racecar"
t = "carrace"
print(isAnagram(s,t))
s = "jar"
t = "jam"
print(isAnagram(s,t))
s="xx"
t="x"
print(isAnagram(s,t))
s="bbcc"
t="ccbc"
print(isAnagram(s,t))
