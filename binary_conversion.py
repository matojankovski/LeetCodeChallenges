a = "11"

def convert_to_dec(a: str):
    result_d = 0
    n = 0
    for i in range(len(a)-1, -1, -1):
        result_d += pow(int(a[i])*2,n)
        n +=1

    return result_d

def convert_to_bin(a: str):
    

convert_to_dec("111")

# for i in range(len(a)-1, -1, -1):
#     print(a[i])




