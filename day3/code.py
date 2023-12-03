import re

def main():
    inputfile = 'input.txt'
    print('Advent of code - Day 3')
    print('Solution 1:', find_solution1(inputfile))
    print('Solution 2:', find_solution2(inputfile))


def find_solution1(filename):
    symbols_dict = {}
    total = 0
    numbers_list = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        lines = [line + '.' for line in lines]
        for row, line in enumerate(lines):
            for column, char in enumerate(line):
                if char != '.' and not char.isdigit():
                    symbols_dict[(row, column)] = char
                    
        for symbol in symbols_dict:
            for row in range(symbol[0] - 1, symbol[0] + 2):
                for column in range(symbol[1] - 1, symbol[1] + 2):
                    if lines[row][column].isdigit():
                        numbers = {}
                        index = column
                        while lines[row][index].isdigit():
                            numbers[(row, index)] = lines[row][index]
                            index -= 1
                        index = column
                        while lines[row][index].isdigit():
                            numbers[(row, index)] = lines[row][index]
                            index += 1
                        if not numbers in numbers_list:
                            numbers_list.append(numbers)
                    
    for number in numbers_list:
        # Sort values by column & add values
        sorted_numbers = sorted(number.items(), key=lambda x: x[0][1])
        sorted_numbers = [x[1] for x in sorted_numbers]
        total += int(''.join(sorted_numbers))
    return total


def find_solution2(filename):
    symbols_dict = {}
    total = 0
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        lines = [line + '.' for line in lines]
        for row, line in enumerate(lines):
            for column, char in enumerate(line):
                if char == '*':
                    symbols_dict[(row, column)] = char

        for symbol in symbols_dict:  
            numbers_list = []
            for row in range(symbol[0] - 1, symbol[0] + 2):
                for column in range(symbol[1] - 1, symbol[1] + 2):
                    if lines[row][column].isdigit():
                        numbers = {}
                        index = column
                        while lines[row][index].isdigit():
                            numbers[(row, index)] = lines[row][index]
                            index -= 1
                        index = column
                        while lines[row][index].isdigit():
                            numbers[(row, index)] = lines[row][index]
                            index += 1
                        if not numbers in numbers_list:
                            numbers_list.append(numbers)

            new_nums = []
            for number in numbers_list:
                # Sort values by column & add values
                sorted_numbers = sorted(number.items(), key=lambda x: x[0][1])
                sorted_numbers = [x[1] for x in sorted_numbers]
                number = int(''.join(sorted_numbers))
                new_nums.append(number)
            if len(new_nums) == 2:
                total += new_nums[0] * new_nums[1]

    return total




if __name__ == '__main__':
    main()