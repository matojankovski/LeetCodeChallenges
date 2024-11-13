def find_divisors(num):
    divisors = []
    i = 28
    while i != 1 :
        if num % i == 0 and num // i != num:
            result = num // i
            divisors.append(result)
        i -= 1
    return divisors

def check_perfect_number(num):
    divisors = []
    i = num
    while i != 1:
        if num % i == 0 and num // i != num:
            result = num // i
            divisors.append(result)
        i -= 1
    if sum(divisors) == num:
        return True
    return False

def check_perfect_number_optimized(num):
    sum = 0
    i = 1
    for i in range(i*i <= num):
        if num % i == 0:
            sum += i
            if i*i != num:
                sum += num / i
    return sum - sum == num




x = 28
print(find_divisors(x))
print(check_perfect_number_optimized(x))
x = 7
print(find_divisors(x))
print(check_perfect_number_optimized(x))
x= 496
print(find_divisors(x))
print(check_perfect_number_optimized(x))







