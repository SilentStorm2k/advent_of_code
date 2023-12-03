import os
import re

def func(input):
    # splitting input into lines
    lines = input.split('\n')
    nums = []
    num_indices = []
    symbols_indices = []
    sum = 0

    # getting all numbers, their location, and the location of all symbols for easy checking 
    for i, text in enumerate(lines):
        nums.insert(i, re.findall(r'[0-9]+', text))
        num_indices.insert(i, [m.span() for m in re.finditer(r'[0-9]+', text)])
        symbols_indices.insert(i, [m.start() for m in re.finditer(r'[^\w\s.]', text)]) 

    # checking if each number in each line is adjacent to a symbol, if so add to sum    
    # num_indices is a list of list of numbers like [[123,34], [23, 34]] where i is the line and j is the location at that line
    for i, list_coords in enumerate(num_indices):
        for j, coords in enumerate(list_coords):
            added = False
            # looking above and below the current line (if its not the first line or last line)
            if i != 0 and i != len(lines)-1:
                # checking every symbols location (above - i-1, current line - i, below - i+1) against the current number's coordinate (coord)
                for symbs in symbols_indices[i]:
                    if symbs in range(coords[0]-1, coords[1]+1) and not added:
                        sum = sum + int(nums[i][j])
                        added = True
                for symbs in symbols_indices[i-1]:
                    if symbs in range(coords[0]-1, coords[1]+1) and not added:
                        sum = sum + int(nums[i][j])
                        added = True
                for symbs in symbols_indices[i+1]:
                    if symbs in range(coords[0]-1, coords[1]+1) and not added:
                        sum = sum + int(nums[i][j])
                        added = True
            # case when checking the numbered coords at the first line (there is no symbols at say line 0)
            if i == 0:
                for symbs in symbols_indices[i]:
                    if symbs in range(coords[0]-1, coords[1]+1) and not added:
                        sum = sum + int(nums[i][j])
                        added = True
                for symbs in symbols_indices[i+1]:
                    if symbs in range(coords[0]-1, coords[1]+1) and not added:
                        sum = sum + int(nums[i][j])
                        added = True
            # case when checking the numbered coords at the last line (there is no symbols after the last line of input)
            if i == len(lines)-1:
                for symbs in symbols_indices[i]:
                    if symbs in range(coords[0]-1, coords[1]+1) and not added:
                        sum = sum + int(nums[i][j])
                        added = True
                for symbs in symbols_indices[i-1]:
                    if symbs in range(coords[0]-1, coords[1]+1) and not added:
                        sum = sum + int(nums[i][j])
                        added = True
    return sum


# when called from ~/Code/repos/advent_of_code$
ex_file = open("2023/day3/puzzle_input/day_3.txt", 'r')
# ex_file = open("2023/day3/puzzle_input/day_3_p1_example.txt", 'r')
input = ex_file.read()
print(f"Answer is : {func(input)}")