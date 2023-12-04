import os
import re
import numpy as np

def func(input):
    input = input.split('\n')
    # print(input)
    total_cards = 0
    copies = np.ones(len(input))
    for row, card in enumerate(input):
        current_points = 0
        c = re.split(r'[\:\|]', card)
        # print(c)
        winners = c[1].split()
        yours = c[2].split()
        for nums in yours:
            if nums in winners:
                current_points = current_points + 1
        current_points_copy = current_points
        i = row + 1
        while(current_points > 0):
            copies[i] = copies[i]+1
            i = i + 1
            current_points = current_points - 1

        # adding the point values for each copy of the cards
        j = copies[row] - 1
        while(j > 0):
            i = row + 1
            current_points = current_points_copy
            j = j - 1
            while(current_points > 0):
                copies[i] = copies[i]+1
                i = i + 1
                current_points = current_points - 1
    for num in copies:
        total_cards = total_cards + num
    return int(total_cards)

# when called from ~/Code/repos/advent_of_code$
ex_file = open("2023/day4/puzzle_input/day_4.txt", 'r')
# ex_file = open("2023/day4/puzzle_input/day_4_p1_example.txt", 'r')
input = ex_file.read()
# print(text)
print(f"Answer is : {func(input)}")