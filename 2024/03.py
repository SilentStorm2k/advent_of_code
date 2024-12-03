import time
from collections import defaultdict, deque
import heapq

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
    n = len(input)
    res = 0
    for i in range(n):
        if input[i:i+4] == "mul(":
            num1, num2 = "", ""
            r = 4
            pre = -1
            for j in range(i+4, i+4+r):
                if j >= n or not input[j].isdigit() or j == i+4+3:
                    pre = j 
                    break
                num1 += input[j]
            if pre == -1 or pre >= n or input[pre] != ",":
                continue
            pre += 1
            for j in range(pre, pre+r):
                if j >= n or not input[j].isdigit() or j == pre+3:
                    pre = j 
                    break
                num2 += input[j]

            if pre >= n or input[pre] != ")":
                continue
            res += int(num1)*int(num2)
    return res
                 
@execute
def p2(input):
    n = len(input)
    res = 0
    enabled = True
    for i in range(n):
        if input[i:i+7] == "don't()":
            enabled = False
        if input[i:i+4] == "do()":
            enabled = True 

        if enabled and input[i:i+4] == "mul(":
            num1, num2 = "", ""
            r = 4
            pre = -1
            for j in range(i+4, i+4+r):
                if j >= n or not input[j].isdigit() or j == i+4+3:
                    pre = j 
                    break
                num1 += input[j]
            if pre == -1 or pre >= n or input[pre] != ",":
                continue
            pre += 1
            for j in range(pre, pre+r):
                if j >= n or not input[j].isdigit() or j == pre+3:
                    pre = j 
                    break
                num2 += input[j]

            if pre >= n or input[pre] != ")":
                continue
            res += int(num1)*int(num2)
    return res
 


def main():
    # when called from ~/Code/repos/advent_of_code$
    input = open("2024/puzzle_input/03_input.txt", 'r').read()
    example = open("2024/puzzle_input/03_example.txt", 'r').read()
    example2 = open("2024/puzzle_input/03_example2.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example2)
    p2(input)

if __name__ == "__main__":
    main()