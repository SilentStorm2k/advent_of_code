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
    inputs, wires = input.split('\n\n')
    inputValues = defaultdict(bool)
    outputValues = {} # key=z00, val=[(g1, valg1),(g2,valg2),gateType,valOfz00]
    z = []
    for inp in inputs.split('\n'):
        k, v = [val.strip() for val in inp.split(':')]
        inputValues[k] = int(v)
    for wire in wires.split('\n'):
        if not wire:
            continue
        gates, output = [val.strip() for val in wire.split('->')]
        g1, gate, g2 = gates.split(' ')
        if output[0] == 'z':
            z.append(output)
        outputValues[output] = [g1, gate, g2, inputValues[output] if output in inputValues else None]
    count = 0
    for g in z:
        if g in inputValues:
            count += 1
    while count < len(z):
        toRemove = []
        for k,v in outputValues.items(): 
            g1, gate, g2, cVal = v
            res = performGateOps (g1,g2,gate,inputValues)
            if res != None:
                toRemove.append(k) 
                if k not in inputValues:
                    count += 1 if k[0] == 'z' else 0
                    inputValues[k] = res
        for k in toRemove:
            del outputValues[k]
    
    binary = [inputValues[g] for g in reversed(sorted(z))] 
    res = 0
    mul = 1
    for i in range(len(binary)-1, -1, -1): 
        res += binary[i]*mul
        mul *= 2
    print(binary)
    return res 

def performGateOps (gate1, gate2, gate, inputValues):
    if gate1 not in inputValues or gate2 not in inputValues:
        return None
    g1 = inputValues[gate1]
    g2 = inputValues[gate2]
    if gate == 'XOR':
        return g1^g2 
    elif gate == 'AND':
        return g1 and g2
    else:
        assert gate == 'OR', print(f"WHAT GATE IS THIS?? {gate}")
        return g1 or g2

                 
@execute
def p2(input):
    inputs, wires = input.split('\n\n')
    inputValues = defaultdict(bool)
    outputValues = {} # key=z00, val=[(g1, valg1),(g2,valg2),gateType,valOfz00]
    z = []
    for inp in inputs.split('\n'):
        k, v = [val.strip() for val in inp.split(':')]
        inputValues[k] = int(v)
    for wire in wires.split('\n'):
        if not wire:
            continue
        gates, output = [val.strip() for val in wire.split('->')]
        g1, gate, g2 = gates.split(' ')
        if output[0] == 'z':
            z.append(output)
        outputValues[output] = [g1, gate, g2, inputValues[output] if output in inputValues else None]
    count = 0
    for g in z:
        if g in inputValues:
            count += 1
    while count < len(z):
        toRemove = []
        for k,v in outputValues.items(): 
            g1, gate, g2, cVal = v
            res = performGateOps (g1,g2,gate,inputValues)
            if res != None:
                toRemove.append(k) 
                if k not in inputValues:
                    count += 1 if k[0] == 'z' else 0
                    inputValues[k] = res
        for k in toRemove:
            del outputValues[k]
    
    binary = [inputValues[g] for g in reversed(sorted(z))] 
    res = 0
    mul = 1
    for i in range(len(binary)-1, -1, -1): 
        res += binary[i]*mul
        mul *= 2
    print(binary)
    return res 


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/24_input.txt", 'r').read()
    example = open("2024/puzzle_input/24_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
