def titleToNumber(columnTitle: str) -> int:
    s = 0
    for index, char in enumerate(columnTitle[::-1]):
        s += (ord(char)-64) * pow(26,index)
    return int(s)

def convertToTitle(columnNumber):
    s = ""
    diff = columnNumber % 26
    while (columnNumber % 26 !=0):
        columnNumber = columnNumber // 26
        diff = int(columnNumber % 26)
        s += "".join(chr(diff+64))
        columnNumber = columnNumber // 26

    s += "".join(chr(1+diff+64))

    return s

print(convertToTitle(29))
print(titleToNumber("A"))