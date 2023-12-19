import re

def sum_id(input, red, green, blue):
    sum = 0
    input = input.split('\n')
    for line in input:
        id = isGamePossible(line, red, green, blue)
        # print(id)
        sum = sum + id
    return sum

def isGamePossible(game, red, green, blue):
    # game = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    pattern = re.split(r'[:;]', game)
    id = int(re.findall(r'[0-9]+',pattern[0])[0])
    pattern = pattern[1:]
    
    for s in pattern:
        red_pattern, green_pattern, blue_pattern = 0,0,0
        words = re.split(r'[,]', s)
        for l in words:
            if re.search(r'red', l):
                red_pattern = red_pattern + int(re.findall(r'[0-9]+', l)[0])
            if re.search(r'green', l):
                green_pattern = green_pattern + int(re.findall(r'[0-9]+', l)[0])
            if re.search(r'blue', l):
                blue_pattern = blue_pattern + int(re.findall(r'[0-9]+', l)[0])
        if red < red_pattern or green < green_pattern or blue < blue_pattern:
            return 0
            
    # print(id)
    # print(f'{red_pattern}, {green_pattern}, {blue_pattern}')
    
    return id


ex_file = open("2023/day 2/puzzle_input/day_2.txt", 'r')
# ex_file = open("2023/day 2/puzzle_input/day_2_example.txt", 'r')
input = ex_file.read()
# print(input)
print(f"Answer is : {sum_id(input, 12, 13, 14)}")
