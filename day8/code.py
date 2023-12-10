from itertools import cycle
from math import lcm

def main():
    inputfile = 'input.txt'
    print('Advent of code - Day 8')
    print('Solution 1:', find_solution1(inputfile))
    print('solution 2:', find_solution2(inputfile))


def get_network(info: list) -> dict:
    network_dict = {}
    for node in info:
        k, v = node.split(' = ')
        v = list(map(lambda x: x.strip(), v.replace(
            '(', '').replace(')', '').split(',')))
        network_dict[k] = (v[0], v[1])
    return network_dict


def solve(starting_point: str, instructions: str, network_dict: dict) -> int:
    instructions = cycle(instructions)
    for steps, instruction in enumerate(instructions):
        if starting_point[-1] == 'Z':
            return steps
        if instruction == 'L':
            starting_point = network_dict[starting_point][0]
        elif instruction == 'R':
            starting_point = network_dict[starting_point][1]


def find_solution1(filename: str) -> int:
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        instructions, _, *info = lines
    network_dict: dict = get_network(info)
    return solve('AAA', instructions, network_dict)
    

def find_solution2(filename: str) -> int:
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        instructions, _, *info = lines
    network_dict = get_network(info)
    pointers = [pointer for pointer in network_dict.keys() if pointer[-1] == 'A']
    return lcm(*[solve(pointer, instructions, network_dict) for pointer in pointers])
    


if __name__ == '__main__':
    main()