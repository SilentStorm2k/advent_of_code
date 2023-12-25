import time
import networkx as nx

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
    input = input.split('\n')
    components = dict()
    edges = nx.Graph()
    for r in input:
        connector, connections = r.strip().split(':')
        connections = [c for c in connections.strip().split(' ')]
        for connection in connections:
            edges.add_edge(connector, connection)
            edges.add_edge(connection, connector)
        components.update({connector:connections})
    
    edges.remove_edges_from(nx.minimum_edge_cut(edges))
    c = list(nx.connected_components(edges))
    if len(c) == 2:
        ans = len(c[0]) * len(c[1])
    return ans

@execute
def p2(input):
    return

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 25/puzzle_input/example.txt" if ex else "2023/day 25/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)