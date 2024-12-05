import functools
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
def p1(input, p2 = False):
    res = 0
    pairs, orders = input.split('\n\n')
    rules = set([tuple(pair.split('|')) for pair in pairs.split('\n')])
    orders = [order.split(',') for order in orders.split('\n')]
    def custom_comparator(x, y):
        if (x, y) in rules:
            return -1
        if (y, x) in rules:
            return 1
        return 0
    for order in orders:
        sortedOrder = sorted(order, key=functools.cmp_to_key(custom_comparator)) 
        if not p2   and order == sortedOrder:
            res += int(sortedOrder[len(sortedOrder)//2])
        if     p2   and order != sortedOrder:
            res += int(sortedOrder[len(sortedOrder)//2])
    return res 
        
@execute
def p2(input):
    return p1.__original(input, p2=True)
 

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/05_input.txt", 'r').read()
    example = open("2024/puzzle_input/05_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()