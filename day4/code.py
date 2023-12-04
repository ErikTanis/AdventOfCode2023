def main():
    inputfile = 'input.txt'
    print('Advent of code - Day 4')
    print('Solution 1:', find_solution1(inputfile))
    print('Solution 2:', find_solution2(inputfile))


def find_solution1(filename):
    total = 0
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            tickets = line.split(':')[1].strip()
            winning_tickets, your_tickets = map(lambda x: set(x.strip().split()), tickets.split('|'))
            wins = len(winning_tickets.intersection(your_tickets))
            if wins > 0:
                total += 2 ** (wins - 1)
    return total


def find_solution2(filename):
    ticket_dict = {}
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            game = int(line.split(':')[0][5:])
            tickets = line.split(':')[1].strip()
            winning_tickets, your_tickets = map(lambda x: set(x.strip().split()), tickets.split('|'))
            wins = len(winning_tickets.intersection(your_tickets))
            ticket_dict[game] = {
                "amount": 1,
                "wins": wins
            }
    
    for ticket in ticket_dict.items():
        if ticket[1]["wins"] > 0:
            for i in range(ticket[0] + 1, ticket[0] + ticket[1]["wins"] + 1):
                ticket_dict[i]["amount"] += ticket[1]["amount"]
    
    return sum(list(map(lambda x: x["amount"], ticket_dict.values())))




if __name__ == '__main__':
    main()