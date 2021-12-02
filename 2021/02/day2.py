
def parse_input (file):
    with open(file, 'r') as f:
        return f.readlines()


input = parse_input('input.txt')

def solution_1 (input):
    x = 0
    y = 0

    for setp in input:
        direction, value = setp.split()
        value = int(value)

        if direction == 'forward':
            x += value
        elif direction == 'up':
            y -= value
        elif direction == 'down':
            y += value
        else:
            print(f"{direction} is an unknown direction!")

    print(f'Part 1: {x * y}')


def solution_2 (input):
    x = 0
    y = 0
    aim = 0

    for setp in input:
        direction, value = setp.split()
        value = int(value)

        if direction == 'forward':
            x += value
            y += aim * value
        elif direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
        else:
            print(f"{direction} is an unknown direction!")

    print(f'Part 2: {x * y}')




solution_1(input)
solution_2(input)
