def main():
    filename = 'input.txt'
    print('Advent of code 2023 - Day 2')
    print('Solution 1:', find_solution1(filename))
    print('Solution 2:', find_solution2(filename))


def find_solution1(filename):
    max_r, max_g, max_b = 12, 13, 14
    gameID_sum = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            gameID, revealed = line.split(':')
            gameID = int(gameID.replace('Game ', ''))
            revealed = revealed.strip()
            revealed_list = list(map(lambda x: x.strip(), revealed.split(';')))
            r, g, b = 0, 0, 0
            for reveal in revealed_list:
                cubes = list(map(lambda x: x.strip(), reveal.split(',')))
                for cube in cubes:
                    if cube.endswith('red'):
                        r = max(r, int(cube.replace(' red', '')))
                    elif cube.endswith('green'):
                        g = max(g, int(cube.replace(' green', '')))
                    elif cube.endswith('blue'):
                        b = max(b, int(cube.replace(' blue', '')))
            if r <= max_r and g <= max_g and b <= max_b:
                gameID_sum += gameID
    return gameID_sum

def find_solution2(filename):
    power_sum = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            gameID, revealed = line.split(':')
            gameID = int(gameID.replace('Game ', ''))
            revealed = revealed.strip()
            revealed_list = list(map(lambda x: x.strip(), revealed.split(';')))
            r, g, b = 0, 0, 0
            for reveal in revealed_list:
                cubes = list(map(lambda x: x.strip(), reveal.split(',')))
                for cube in cubes:
                    if cube.endswith('red'):
                        r = max(r, int(cube.replace(' red', '')))
                    elif cube.endswith('green'):
                        g = max(g, int(cube.replace(' green', '')))
                    elif cube.endswith('blue'):
                        b = max(b, int(cube.replace(' blue', '')))
            
            power_sum += (r*g*b)
    return power_sum


if __name__ == '__main__':
    main()