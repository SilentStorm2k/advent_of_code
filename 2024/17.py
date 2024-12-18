import time
import re
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
    registers, program = input.split('\n\n')
    registers = [int(ele.split(':')[1]) for ele in registers.split('\n')]
    program = [int(ele) for ele in program.split(':')[1].strip().split(',')]
    output = runProgram(registers, program)
    for i in range(1,1000):
        registers[0] = i
        print(i, runProgram(registers, program))
    return ",".join(map(str, output)) 
                 
@execute
def p2(input):
    registers, program = input.split('\n\n')
    registers = [int(ele.split(':')[1]) for ele in registers.split('\n')]
    program = [int(ele) for ele in program.split(':')[1].strip().split(',')]
    q = deque()
    for i in range(1,8):
        q.append(i)
    print(0, q)
    mul = 1
    while q:
        length = len(q)
        for _ in range(length):
            A = q.popleft()
            factor = 8**mul
            start = max(1, factor*A)
            end = start + factor 
            # print(start, end)
            for i in range(start, end):
                registers[0] = i
                curOutput = runProgram(registers, program)
                # print("i =", i, curOutput)
                m = len(curOutput)
                if program == curOutput:
                    return i
                if program[-m:] == curOutput:
                    # print(m, program[-m:], curOutput)
                    q.append(i)
                    # print(A, curOutput, m, program[-m], curOutput[0])
        print(mul, q)
        mul += 1
    return A

def runProgram (registers, program):
    # print(registers)
    idx = 0
    end = len(program)
    output = [] 
    while idx < end:
        curOut, registers, idx = operate(registers, program, idx)
        if curOut != None:
            output.append(curOut)
    return output
 
def operate (registers, program, idx):
    A, B, C = registers
    output = None
    opcode, operand = program[idx], program[idx+1]
    def combo (lit, registers):
        if 0 <= lit <= 3:   
            return lit
        elif lit == 4:
            return registers[0] 
        elif lit == 5:
            return registers[1]
        elif lit == 6:
            return registers[2]
        else:
            assert lit == 7, "Combo operand 7 is reserved and should not appear in valid programs."
            raise ValueError("Combo operand 7 is reserved and will not appear in valid programs.")

    nxIdx = idx+2
    if opcode == 0:
        # adv, performs division
        A = A // 2**combo(operand, registers)
    elif opcode == 1:
        # bxl, bitwise xor 
        B = B^operand
    elif opcode == 2:
        # bst, combo mod 8
        B = combo(operand, registers)%8
    elif opcode == 3:
        # jnz, moves pointer
        if A != 0:
            nxIdx = operand
    elif opcode == 4:
        # bxc, bitwise xor
        B = B ^ C
    elif opcode == 5:
        # out register, print output
        output = combo(operand, registers)%8
    elif opcode == 6:
        # bdv, division but stores in B register 
        B = A // 2**combo(operand, registers)
    elif opcode == 7:
        # cdv, division but stores in C register
        C = A // 2**combo(operand, registers)
    else:
        raise ValueError(f"Opcode {opcode} is invalid")

    return output, [A, B, C], nxIdx


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/17_input.txt", 'r').read()
    example = open("2024/puzzle_input/17_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    # p1(input)
    print("\nPart 2:")
    p2(example)
    # p2(input)

if __name__ == "__main__":
    main()