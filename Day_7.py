import requests
import numpy
import re

headers = {
    "cookie" : "_ga=GA1.2.1903562712.1678870843; session=53616c7465645f5fe2704c12c5baa88bb4156d4d352fd315b6c3721bead0a4bc869f2aab0112cf8fb668920f06518b5db604181031b1528163cf3856fe1db78b; _gid=GA1.2.169835652.1681208173"
}

# vstup = requests.get('https://adventofcode.com/2022/day/7/input', headers=headers).text.splitlines()

vstup = ["$ cd /", "$ ls", "dir a", "14848514 b.txt", "8504156 c.dat", "dir d", "$ cd a", "$ ls", "dir e", "29116 f", "2557 g",
         "62596 h.lst", "$ cd e", "$ ls", "584 i", "$ cd ..", "$ cd ..", "$ cd d", "$ ls", "4060174 j", "8033020 d.log", "5626152 d.ext", "7214296 k"]
directory = []
print(vstup)

class Directory:
    def __init__(self):
        pass




