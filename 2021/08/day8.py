# Advent of Code - 2021
# --- Day 8: Seven Segment Search ---

# Data inport function
import sys
sys.path.append('C:/Code/Advent of Code/helpers/')

import time
import input

#data = input.lines('C:\Code\Advent of Code\\2021\\08\example.txt')
data = input.lines('C:\Code\Advent of Code\\2021\\08\input.txt')

def part1(data):
    sum = 0
    for line in data:
        sum += len(
            [cell for cell in line.split('|')[1].split()
            if len(cell) in [2,3,4,7]]
        )
    return sum


def part2(data):
    sum = 0

    displays = [
    tuple(part.split() for part in line.split(" | "))
        for line in data
    ]

    for digits, challenge in displays:
        d1 = set(list([ digit for digit in digits if len(digit) == 2 ][0]))
        d7 = set(list([ digit for digit in digits if len(digit) == 3 ][0]))
        d4 = set(list([ digit for digit in digits if len(digit) == 4 ][0]))
        d8 = set(list([ digit for digit in digits if len(digit) == 7 ][0]))
        d9 = set(list([ digit for digit in digits if len(digit) == 6 and len( set(list(digit)) - set.union(d4, d7) ) == 1 ][0]))
        d0 = set(list([ digit for digit in digits if len(digit) == 6 and set(list(digit)) != d9 and all(s in digit for s in d7) ][0]))
        d6 = set(list([ digit for digit in digits if len(digit) == 6 and set(list(digit)) != d9 and set(list(digit)) != d0 ][0]))
        d3 = set(list([ digit for digit in digits if len(digit) == 5 and all(s in digit for s in d7) ][0]))
        e = min(d8 - d9)
        d2 = set(list([ digit for digit in digits if len(digit) == 5 and e in digit ][0]))
        d5 = set(list([ digit for digit in digits if len(digit) == 5 and set(list(digit)) != d3 and set(list(digit)) != d2 ][0]))

        ds = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]

        n = ''
        for digit in challenge:
            n = n + str(ds.index(set(list(digit))))

        sum = sum + int(n)
    return sum

print('\33[91mPART 1\33[0m')
time_start = time.perf_counter()
print(f'Result: {part1(data)}')
time_end = time.perf_counter()
print(f'Elapsed time: {time_end - time_start:0.5f} secs.') 


print('\33[91mPART 2\33[0m')
time_start = time.perf_counter()
print(f'Result: {part2(data)}')
time_end = time.perf_counter()
print(f'Elapsed time: {time_end - time_start:0.5f} secs.') 