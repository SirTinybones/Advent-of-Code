# --- Day 7: The Treachery of Whales ---
# https://adventofcode.com/2021/day/7

from statistics import median, mean
import time

def parse_input (file):
    return [int(i) for i in open(file).read().split(",")]

data = parse_input('C:\Code\Advent of Code\\2021\\07\input.txt')

# PART 1
def part1(data):
    alignment_point = int(median(data))
    return sum([abs(alignment_point - pos) for pos in data])



# PART 2
# The fuel are calculated using the triangular number sequence
# Formula: n^th number = n(n+1)/2

# Caluctate the nth number in the triangular number sequence
def tri(n):
    return n*(n+1)/2

# Simple calculation of Euclidean distance between two points p and q
def dist(p, q):
    return abs(p-q)

def part2(data):
    alignment_point = int(mean(data))
    return int(min([
        sum(tri(dist(alignment_point, pos)) for pos in data)
    ]))


puzzel_name = 'The Treachery of Whales'
banner_lights = '\33[31m•\33[32m•'

print(banner_lights*20 + '\33[0m')
print('\33[32mPuzzle: ' + puzzel_name + '\33[0m')
print(banner_lights*20 + '\33[0m')


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
