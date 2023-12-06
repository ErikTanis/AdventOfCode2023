def main():
    inputfile = 'input.txt'
    print('Advent of code - Day 6')
    print('Solution 1:', find_solution1(inputfile))
    print('Solution 2:', find_solution2(inputfile))


def get_distance(hold_time, total_time):
    return (total_time - hold_time) * hold_time


def find_solution1(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        times = [int(num) for num in lines[0].split(':')[1].strip().split()]
        distances = [int(num) for num in lines[1].split(':')[1].strip().split()]
        total = 1
        for time, distance in zip(times, distances):
            win_options = []
            for i in range(time):
                if get_distance(i, time) > distance:
                    win_options.append(i)
            total *= len(win_options)
    return total


def find_solution2(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        time = int(''.join([num for num in lines[0] if num.isdigit()]))
        distance = int(''.join([num for num in lines[1] if num.isdigit()]))
        win_options = []
        for i in range(time):
            if get_distance(i, time) > distance:
                win_options.append(i)
        return len(win_options)

if __name__ == '__main__':
    main()