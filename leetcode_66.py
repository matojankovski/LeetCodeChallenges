digits = [1,2,3]

def plusOne(digits):
    numbers = "".join(map(str,digits))
    numbers = int(numbers)+1
    print((numbers))
    res = [int(x) for x in str(numbers)]
    print(res)


plusOne(digits)