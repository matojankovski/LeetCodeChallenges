import requests
import numpy
import re

headers = {
    "cookie" : "_ga=GA1.2.1876342333.1682592811; _gid=GA1.2.1329485501.1686050156; session=53616c7465645f5f0360fe87f95210adcb7b88fafe77fddc8fb68b65b9650fd66a5101174ad6db89db87d6c5891946d549218f8be354d8003ab6926e7cadcf0f"
}

vstup = requests.get('https://adventofcode.com/2022/day/8/input', headers=headers).text.splitlines()


new_list = []

for riadok in range(len(vstup)):
    new_list.append([i for i in vstup[riadok]])
# print(new_list)

# print(new_list[0][0])
# print(new_list[0])
sum = 0
def check_line_of_view(area, position_x, position_y):
    if area[position_x-1, position_y] < current_tree_position and area[position_x, position_y-1] < current_tree_position and area[position_x+1, position_y] < current_tree_position and area[position_x, position_y+1] < current_tree_position:
        return True
    else:
        return False

for riadok in range(1, len(new_list)-1):
    for stlpec in range(1, len(new_list[0])-1):
        print(new_list[riadok][stlpec])
        if check_line_of_view(new_list, riadok, stlpec):
            sum +=1

print(sum)




