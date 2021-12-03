# Advent of Code - 2021
# --- Day 3: Binary Diagnostic ---
# https://adventofcode.com/2021/day/3

def parse_input (file):
    with open(file, 'r') as f:
        return f.readlines()


# --- Part One --- 
def solution_1(input):
    gamma  = ''
    epsilon  = ''

    for bit in zip(*input):
        if bit.count('1') > bit.count('0'):
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    print(f'Part 1: {int(gamma,2) * int(epsilon,2)}')



# --- Part Two ---

# Find the most common bit
def most_common_bit(input: list[str], n=0) -> str | None:
    ones, zeros = 0, 0
    for line in input:
        if line[n] == '1':
            ones += 1
        else:
            zeros += 1

    if ones == zeros:
        return None

    elif ones > zeros:
        return '1'

    return '0'

def filter_bits(numbers: list[str], most_common=True):  # isnt that fun?
    for i in range(len(numbers[0])):
        mc = most_common_bit(numbers, i)
        if mc is None:
            mc = '1'

        if not most_common:
            if mc == '1':
                mc = '0'
            else:
                mc = '1'

        new_numbers = [n for n in numbers if n[i] == mc]
        if len(new_numbers) == 0:
            break

        numbers = new_numbers

    assert len(numbers) == 1, f'{numbers=}'
    return numbers[0]

def solution_2(input: str) -> str:
    o2 = int(filter_bits(input, True),2)
    co2 = int(filter_bits(input, False),2)

    print(f'Part 2: {o2 * co2}')


solution_1(parse_input('input.txt'))
solution_2(parse_input('input.txt'))