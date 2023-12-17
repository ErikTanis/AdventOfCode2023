def main() -> None:
    inputfile = 'input.txt'
    print('Advent of code - Day 15')
    print('Solution 1:', find_solution1(inputfile))
    print('Solution 2:', find_solution2(inputfile))


def hash(value: str) -> int:
    total = 0
    for character in value:
        total += ord(character)
        total *= 17
        total %= 256
    return total

def find_solution1(filename: str) -> int:
    with open(filename) as file:
        values = file.read().split(',')
    hashes = [hash(x) for x in values]
    return sum(hashes)

def find_solution2(filename: str) -> int:
    total = 0
    boxes = {}
    with open(filename) as file:
        actions = file.read().split(',')
    for action in actions:
        if '=' in action:
            label, length = action.split('=')
            box_num = hash(label)
            if box_num in boxes:
                boxes[box_num][label] = length
            else:
                boxes[box_num] = {label: length}
        if '-' in action:
            label = action[:-1]
            box_num = hash(label)
            if box_num in boxes:
                if label in boxes[box_num]:
                    del boxes[box_num][label]
    
    for box_num, lenses in boxes.items():
        for i, length in enumerate(lenses.values()):
            total += (box_num + 1) * (i + 1) * int(length)
    
    return total


if __name__ == '__main__': 
    main()