import re

def sum(input):
    sum = 0
    input = input.split('\n')
    for line in input:
        val = power_sum(line)
        # print(id)
        sum = sum + val
    return sum

def power_sum(game):
    # game = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    pattern = re.split(r'[:;]', game)
    # id = int(re.findall(r'[0-9]+',pattern[0])[0])
    pattern = pattern[1:]
    red_pattern, green_pattern, blue_pattern = 0,0,0
    for s in pattern:    
        words = re.split(r'[,]', s)
        for l in words:
            if re.search(r'red', l):
                red_pattern = red_pattern if int(re.findall(r'[0-9]+', l)[0]) < red_pattern else int(re.findall(r'[0-9]+', l)[0])
            if re.search(r'green', l):
                green_pattern = green_pattern if int(re.findall(r'[0-9]+', l)[0]) < green_pattern else int(re.findall(r'[0-9]+', l)[0])
            if re.search(r'blue', l):
                blue_pattern = blue_pattern if int(re.findall(r'[0-9]+', l)[0]) < blue_pattern else int(re.findall(r'[0-9]+', l)[0])
            
    # print(id)
    # print(f'{red_pattern}, {green_pattern}, {blue_pattern}')
    power_sum = red_pattern*green_pattern*blue_pattern
    
    return power_sum


ex_file = open("advent_of_code/2023/day2/puzzle_input/day_2.txt", 'r')
# ex_file = open("advent_of_code/2023/day2/puzzle_input/day_2_example.txt", 'r')
input = ex_file.read()
# print(input)
print(f"Answer is : {sum(input)}")
