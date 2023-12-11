from itertools import combinations

def main():
    inputfile = 'input.txt'
    print('Advent of code - Day 11')
    print('Solution 1:', find_solution1(inputfile))
    print('Solution 2:', find_solution2(inputfile))


def add_space(galaxy_dict: dict, space: int, space_columns: list, space_rows: list) -> dict:
    for k, v in galaxy_dict.items():
        x = v[0]
        y = v[1]
        empty_column_amount = len([_ for _ in space_columns if _ < x])
        empty_row_amount = len([_ for _ in space_rows if _ < y])
        x += empty_column_amount * space
        y += empty_row_amount * space
        galaxy_dict[k] = (x,y)
    return galaxy_dict

def solve(filename: str, space: int):
    total = 0
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        grid = [list(line) for line in lines]
    
    columns = {}
    space_columns = []
    space_rows = []
    for y, row in enumerate(grid):
        if set(row) == {'.'}:
            space_rows.append(y)
        for x, character in enumerate(row):
            if x in columns:
                columns[x].add(character)
            else:
                columns[x] = {character}
    
    for k,v in columns.items():
        if v == {'.'}:
            space_columns.append(k)

    galaxy_dict = {}
    for y, row in enumerate(grid):
        for x, character in enumerate(row):
            if character == '#':
                galaxy_dict[len(galaxy_dict)+1] = (x,y)

    galaxy_dict = add_space(galaxy_dict, space, space_columns, space_rows)

    for first, second in combinations(galaxy_dict.values(), 2):
        x_diff = abs(first[0] - second[0])
        y_diff = abs(first[1] - second[1])
        total += x_diff + y_diff
    
    return total


def find_solution1(filename: str) -> int:
    return solve(filename, 1)

def find_solution2(filename: str) -> int:
    return solve(filename, 999999)
    


if __name__ == '__main__':
    main()