import os

def calibration_sum(calibration_text):
    text = calibration_text.split()
    sum = 0
    for words in text:
        first_num_flag = True
        for letter in words:
            if (letter.isnumeric() and first_num_flag):
                first_num = letter
                first_num_flag = False
            if (letter.isnumeric()):
                last_num = letter
        # print(f"Numbers = {first_num} , {last_num}")
        sum = sum + int(first_num)*10 + int(last_num)
    return sum

ex_file = open("advent_of_code/2023/day1/puzzle_input/day_1_p1.txt", 'r')
# ex_file = open("advent_of_code/2023/day1/puzzle_input/day_1_p1_example.txt", 'r')
text = ex_file.read()
# print(text)
print(f"Answer is : {calibration_sum(text)}")
