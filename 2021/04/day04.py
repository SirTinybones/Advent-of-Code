# --- Day 4: Giant Squid ---
# ref: https://adventofcode.com/2021/day/4


input = open('C:\Code\Advent of Code\\2021\\04\input.txt').read()

def bingo(board, calls):
    for i in range(5):
        if all(board[i][j] in calls for j in range(5)):
            return True
        if all(board[j][i] in calls for j in range(5)):
            return True

    return False

def score(board, calls):
    unmarked = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] not in calls:
                unmarked += board[i][j]

    return unmarked * calls[-1] # assume calls isn't longer than it needs to be

def solve(inp):
    sequence, *boards = inp.split("\n\n")

    sequence = [int(x) for x in sequence.split(",")]
    boards = [
        [[int(num) for num in line.split()] for line in board.strip().split("\n")]
            for board in boards
    ]

    order = {}

    for i in range(1, len(sequence)):
        for j, board in enumerate(boards):
            if j in order.keys():
                continue

            if bingo(board, sequence[:i]):
                order[j] = i

    first = min(order, key=order.get)
    last = max(order, key=order.get)

    return (
        score(boards[first], sequence[:order[first]]),
        score(boards[last], sequence[:order[last]])
    )

solve(input)