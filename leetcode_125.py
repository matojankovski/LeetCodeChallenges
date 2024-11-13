s1 = "race a car"
s2 = "A man, a plan, a canal: Panama"
def remove_non_alphanumeric(text):
    return ''.join(char for char in text if char.isalnum())

def isPalindrome(s: str):
    s = ''.join(char for char in s if char.isalnum())
    s = s.lower()
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

print(isPalindrome(s1))
print(isPalindrome(s2))

string = "Hello, World! 123"
cleaned_string = remove_non_alphanumeric(string)
print(cleaned_string)



