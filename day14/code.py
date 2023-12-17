def main() -> None:
    inputfile = 'input.txt'
    print('Advent of code - Day 14')
    print('Solution 1:', find_solution1(inputfile))
    print('Solution 2:', find_solution2(inputfile))


def convert_row_column(lines: list) -> list:
    columns = {}
    for line in lines:
          for i, character in enumerate(line):
                if i in columns:
                    columns[i].append(character)
                else:
                    columns[i] = [character]
    return [*columns.values()]


def roll_north(column: list) -> list:
    for i, character in enumerate(column):
        if character != 'O':
            continue
        if i > 0 and column[i-1] == '.':
            column = column[:i-1] + ['O', '.'] + column[i+1:]
    for i, character in enumerate(column):
        if character != 'O':
            continue
        if i > 0 and column[i-1] == '.':
            return roll_north(column)
    return column

def roll_east(row: list) -> list:
    return roll_north(row)

def roll_south(column: list) -> list:
    return roll_north(column[::-1])[::-1]

def roll_west(row: list) -> list:
    return roll_south(row)

def find_solution1(filename: str) -> int:
    total = 0
    with open(filename) as file:
        lines = file.read().splitlines()
    columns = convert_row_column(lines)
    for column in columns:
        column = roll_north(column)
        for i, character in enumerate(column):
            if character == 'O':
                multiplier = len(column) - i
                total += multiplier
    return total


def find_solution2(filename: str) -> int:
    total = 0
    with open(filename) as file:
        lines = file.read().splitlines()
    columns = convert_row_column(lines)
    loops = 1_000_000_000
    for loop_num in range(loops):
        for i, column in enumerate(columns):
            columns[i] = roll_north(column)
        rows = convert_row_column(columns)
        for i, row in enumerate(rows):
            rows[i] = roll_east(row)
        columns = convert_row_column(rows)
        for i, column in enumerate(columns):
            columns[i] = roll_south(column)
        rows = convert_row_column(columns)
        for i, row in enumerate(rows):
            rows[i] = roll_west(row)
        columns = convert_row_column(rows)
        if loop_num == loops - 1:
            for column in columns:
                for i, character in enumerate(column):
                    if character == 'O':
                        multiplier = len(column) - i
                        total += multiplier
    return total


if __name__ == '__main__':
    main()
