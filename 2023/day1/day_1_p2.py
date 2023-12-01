import os

def calibration_sum(calibration_text):
    text = calibration_text.split()
    sum = 0
    numbered_letters = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}
    for words in text:
        first_num_flag = True
        first_let_flag = True
        let1_loc, let2_loc, num1_loc, num2_loc = 1000, -1000, 1000, -1000
        first_let, last_let, first_num, last_num = -1, -1, -1, -1

        for i, letter in enumerate(words):
            for num in numbered_letters.keys():
                if (num in words[i:i+5] and first_let_flag):
                    first_let = numbered_letters.get(num)
                    let1_loc = words[i:i+5].find(num) + i
                    first_let_flag = False 
                if (num in words[i:i+5]):
                    last_let = numbered_letters.get(num)
                    let2_loc = words[i:i+5].find(num) + i
            if (letter.isnumeric() and first_num_flag):
                first_num = letter
                first_num_flag = False
                num1_loc = i
            if (letter.isnumeric()):
                last_num = letter
                num2_loc = i
        
        tens_place = int(first_let)*10 if let1_loc < num1_loc else int(first_num)*10
        ones_place = int(last_let) if let2_loc > num2_loc else int(last_num)
        num = ones_place + tens_place
        # print(f"first letter: {first_let}, first number: {first_num}, Last letter: {last_let}, last number: {last_num}")
        # print(num)
        # print(f"Numbers = {first_num} , {last_num}")
        sum = sum + num
    return sum

ex_file = open("advent_of_code_2023/day1/puzzle_input/day_1_p1.txt", 'r')
# ex_file = open("advent_of_code_2023/day1/puzzle_input/day_1_p2_example.txt", 'r')
text = ex_file.read()
# print(text)
print(f"Answer is : {calibration_sum(text)}")
