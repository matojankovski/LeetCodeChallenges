
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    hash_s, hash_t = {}, {}

    for i, n in enumerate(s):
        hash_s[s[i]] = hash_s.get(n, 0) + 1
        hash_t[t[i]] = hash_t.get(n, 0) + 1

    print(hash_s)
    print(hash_t)
    if len(hash_s) != len(hash_t):
        return False
    if sorted(hash_s.values()) != sorted(hash_t.values()):
        return False
    return True


s = "egg"
t = "add"

print(isIsomorphic(s, t))
s = "foo"
t = "bar"
print(isIsomorphic(s, t))

