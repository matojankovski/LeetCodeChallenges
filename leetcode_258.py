def addDigits( num: int) -> int:
    while num >= 10:
        num = sum(int(digit) for digit in str((num)))
    return num

def addDigits1(num: int) -> int:
    while num >= 10:  # Repeat until a single digit
        num = sum(int(digit) for digit in str(num))  # Sum the digits
    return num


num = 10
print(addDigits(num))
print(addDigits1(num))