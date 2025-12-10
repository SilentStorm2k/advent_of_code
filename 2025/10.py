from pulp import *
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
    # if need to reuse p1 w/o decorator use : p1.__original(input)
    wrapper.__original = func
    return wrapper


@execute
def p1(input):
    # create bitmask for final output, each button will be a bitmask
    # we will do a multipoint bfs on buttons (optimization: dont press same button consequtively)
    # when out current bits match final output bitmask, we return tree depth
    def makeStateBitmask(state):
        res = 0
        N = len(state)
        for idx, ele in enumerate(list(state)):
            if ele == '#':
                res |= 1 << N-idx-1
        return res

    def makeButtonBitmask(button, N):
        res = 0
        for ele in button:
            res |= 1 << N-ele-1
        return res

    def bfs(finalState, buttons):
        if finalState == 0:
            return 0
        depth = 1
        q = deque([(button, [button]) for button in buttons])
        seen = set()
        while len(q) > 0:
            for i in range(len(q)):
                state, prevButton = q.popleft()
                if state == finalState:
                    return depth
                if state in seen:
                    continue
                seen.add(state)
                for button in buttons:
                    if button != prevButton[-1]:
                        newState = state ^ button
                        prevButton.append(button)
                        q.append((newState, list(prevButton)))
                        prevButton.pop()
            depth += 1
        return -1

    presses = 0
    machines = input.split('\n')
    for machine in machines:
        machine = machine.split(' ')
        finalState, buttons, joltages = machine[0], machine[1:-1], machine[-1]
        finalState = re.findall(r'\[(.*)\]', finalState)[0]
        buttons = [[int(i) for i in re.findall(r'\((.*)\)', button)[0].split(',')]
                   for button in buttons]
        joltages = [int(i) for i in re.findall(
            r'\{(.*)\}', joltages)[0].split(',')]
        N = len(finalState)
        finalState = makeStateBitmask(finalState)
        buttons = [makeButtonBitmask(button, N) for button in buttons]
        presses += bfs(finalState, buttons)

    return presses


@execute
def p2(input):

    def bfs(buttons, finalState):
        finalState = tuple(finalState)
        startState = [0]*len(finalState)
        q = deque([tuple(startState)])
        depth = 0
        seen = set()
        while len(q):
            for i in range(len(q)):
                curState = q.popleft()
                if curState == finalState:
                    return depth
                if curState in seen:
                    continue
                seen.add(curState)
                for button in buttons:
                    nxtState = list(curState)
                    for idx in button:
                        nxtState[idx] += 1
                    q.append(tuple(nxtState))
            depth += 1
        return -1

    minPresses = 0
    machines = input.split('\n')
    for idx, machine in enumerate(machines):
        machine = machine.split(' ')
        buttons, joltages = machine[1:-1], machine[-1]
        buttons = [[int(i) for i in re.findall(r'\((.*)\)', button)
                    [0].split(',')] for button in buttons]
        joltages = [int(ele)
                    for ele in re.findall(r'\{(.*)\}', joltages)[0].split(',')]
        # minPresses += bfs(buttons, joltages)

        prob = LpProblem("Machine button clicks", LpMinimize)
        buttonPresses = [LpVariable(
            f'bp{i}', lowBound=0, cat=LpInteger) for i in range(len(buttons))]
        prob += lpSum(buttonPresses)

        constraints = defaultdict(list)
        for buttonIdx, button in enumerate(buttons):
            for idx in button:
                constraints[idx].append(buttonPresses[buttonIdx])

        for idx, val in enumerate(joltages):
            prob += lpSum(constraints[idx]) <= val
            prob += lpSum(constraints[idx]) >= val

        # for button in buttons:
        prob.solve(PULP_CBC_CMD(msg=False))
        minPresses += value(prob.objective)

    return int(minPresses)


def main():
    # when called from ~/advent_of_code$
    input = open("2025/puzzle_input/10_input.txt", 'r').read()
    example = open("2025/puzzle_input/10_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)


if __name__ == "__main__":
    main()
