def main():
    inputfile = 'input.txt'
    print('Advent of code - Day 7')
    print('Solution 1:', find_solution1(inputfile))
    print('Solution 2:', find_solution2(inputfile))


def deck_score1(deck: str) -> list:
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    points = [cards.index(card) for card in deck]
    return points


def deck_score2(deck: str) -> list:
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    points = [cards.index(card) for card in deck]
    return points


def get_points1(hand: str) -> int:
    if hand.count(hand[0]) == 5:
        return 1
    hand = sorted(hand, key=hand.count, reverse=True)
    for card in hand:
        if hand.count(card) == 4:
            return 2
        elif hand.count(card) == 3:
            if len(set(hand)) == 2:
                return 3
            else:
                return 4
        elif hand.count(card) == 2:
            if len(set(hand)) == 3:
                return 5
            else:
                return 6
        return 7


def get_points2(hand: str) -> list:
    if 'J' not in hand:
        return [get_points1(hand)]
    points = []
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for card in cards:
        new_hand = hand.replace('J', card, 1)
        points.extend(get_points2(new_hand))
    return points


def find_solution1(filename: str):
    hands = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            hand, bet = line.split()
            bet = int(bet)
            hands.append( (hand, get_points1(hand), bet) )

    sorted_hands = sorted(hands, key= lambda x: (x[1], deck_score1(x[0])), reverse=True)
    total = sum([(i+1) * hand[2] for i, hand in enumerate(sorted_hands)])
    return total


def find_solution2(filename):
    hands = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            hand, bet = line.split()
            bet = int(bet)
            hands.append( (hand, min(get_points2(hand)), bet) )

    sorted_hands = sorted(hands, key= lambda x:(x[1], deck_score2(x[0])), reverse=True)
    total = sum([(i+1) * hand[2] for i, hand in enumerate(sorted_hands)])
    return total


if __name__ == '__main__':
    main()
