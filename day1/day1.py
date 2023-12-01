
def main():
    input_file = 'd1.txt'
    print('Advent of code 2023 - Day 1')
    print('Solution 1:', find_solution1(input_file))
    print('Solution 2:', find_solution2(input_file))


def find_solution1(inputfile):
    total = 0
    text_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open(inputfile, 'r') as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            numbers = [x for x in line if x.isdigit()]
            line_total = numbers[0] + numbers[-1]
            total += int(line_total)

    return total

def find_solution2(inputfile):
    total = 0
    text_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open(inputfile, 'r') as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            for text_num in text_nums:
                line = line.replace(text_num, text_num[0] + str(text_nums.index(text_num) + 1) + text_num[-1])
            numbers = [x for x in line if x.isdigit()]
            line_total = numbers[0] + numbers[-1]
            total += int(line_total)

    return total

if __name__ == '__main__':
    main()