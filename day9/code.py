def main():
    inputfile = 'input.txt'
    print('Advent of code - Day 9')
    print('Solution 1:', find_solution1(inputfile))
    print('Solution 2:', find_solution2(inputfile))


def find_next(seq: list[int]) -> int:
    next_seqs: list[list[int]] = [seq]
    while not set(next_seqs[-1]) == {0}:
        new_seq = []
        for i, num in enumerate(next_seqs[-1]):
            if i == len(next_seqs[-1]) -1: continue
            new_seq.append(next_seqs[-1][i+1] - next_seqs[-1][i])
        next_seqs.append(new_seq)
    return sum([num[-1] for num in next_seqs])


def find_solution1(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            seq = [int(num) for num in line.split()]
            total += find_next(seq)
    return total

def find_solution2(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            seq = [int(num) for num in line.split()]
            total += find_next(seq[::-1])
    return total


if __name__ == '__main__':
    main()