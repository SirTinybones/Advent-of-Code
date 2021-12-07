# Advent of Code - 2021
# --- Day 2: Dive! ---

def parse_input (file):
    with open(file, 'r') as f:
        return f.readlines()


input = parse_input('C:\Code\Advent of Code\\2021\\02\input.txt')

# PART 1 #
def part_1 (input):
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

    return int(x * y)


# PART 2 #
def part_2 (input):
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

    return int(x * y)


print(f'Part 1: {part_1(input)}')
print(f'Part 2: {part_2(input)}')
