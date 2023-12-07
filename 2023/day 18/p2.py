import time

def execute(func):
    def wrapper(*args):   
        t1 = time.time()
        print(f'Answer is : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    return wrapper 

@execute
def func(input):
    return 

# when called from ~/Code/repos/advent_of_code$
ex = 1
input = open("2023/day 18/puzzle_input/example.txt" if ex else "2023/day 18/puzzle_input/input.txt", 'r').read()
func(input)