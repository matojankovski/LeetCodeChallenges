def isPalindrome(x):
    string = str(x)
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

print(isPalindrome(101))