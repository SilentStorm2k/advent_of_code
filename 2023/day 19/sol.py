import time

def execute(func):
    def wrapper(*args):   
        t1 = time.time()
        print(f'Answer for {func.__name__} : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    wrapper.__original = func # if need to reuse p1 w/o decorator use : p1.__original(input)
    return wrapper 

@execute
def p1(input):
    return 

@execute
def p2(input):
    return

# when called from ~/Code/repos/advent_of_code$
ex = 1
input = open("2023/day 19/puzzle_input/example.txt" if ex else "2023/day 19/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)