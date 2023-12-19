import os
import re

def func(input):
    # splitting input into lines
    lines = input.split('\n')
    nums = []
    num_indices = []
    # in this case, there is only one symbol we look for "*"
    symbols_indices = []
    sum = 0

    # getting all numbers, their location, and the location of all symbols for easy checking 
    for i, text in enumerate(lines):
        nums.insert(i, re.findall(r'[0-9]+', text))
        num_indices.insert(i, [m.span() for m in re.finditer(r'[0-9]+', text)])
        symbols_indices.insert(i, [m.start() for m in re.finditer(r'[*]', text)]) 

    # we check the location of every "*", and verify whether it is a gear (has only 2 adjacent numbers [including diagonal])
    for i, lis_gears in enumerate(symbols_indices):
        for j, gear_index in enumerate(lis_gears):
            gear_ratio = []
            # checking numbers above, current and below the current line
            for k, n in enumerate(num_indices[i-1]):
                # if number is adjacent, add numbers to potential gear list
                if gear_index in range(n[0]-1, n[1]+1):
                    gear_ratio.append(nums[i-1][k])
            for k, n in enumerate(num_indices[i]):
                # if number is adjacent, add numbers to potential gear list
                if gear_index in range(n[0]-1, n[1]+1):
                    gear_ratio.append(nums[i][k])
            for k, n in enumerate(num_indices[i+1]):
                # if number is adjacent, add numbers to potential gear list
                if gear_index in range(n[0]-1, n[1]+1):
                    gear_ratio.append(nums[i+1][k])

            # if the gear_ratio list only has 2 elements (hence a valid gear), add its product to sum
            if len(gear_ratio) == 2:
                sum = sum + int(gear_ratio[0])*int(gear_ratio[1])
                # print(f"sum = {sum}, 2 nums = {gear_ratio}")

    return sum

# when called from ~/Code/repos/advent_of_code$
ex_file = open("2023/day 3/puzzle_input/day_3.txt", 'r')
# ex_file = open("2023/day 3/puzzle_input/day_3_p1_example.txt", 'r')
input = ex_file.read()
print(f"Answer is : {func(input)}")