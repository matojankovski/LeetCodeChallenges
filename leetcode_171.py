def titleToNumber(columnTitle: str) -> int:
    s = 0
    for index, char in enumerate(columnTitle[::-1]):
        s += (ord(char)-64) * pow(26,index)
    return int(s)



columnTitle1 = "Z"
print(titleToNumber(columnTitle1))
columnTitle2 = "AA"
print(titleToNumber(columnTitle2))
columnTitle3 = "ZY"
print(titleToNumber(columnTitle3))
