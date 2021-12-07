# --- Day 7: The Treachery of Whales ---
# https://adventofcode.com/2021/day/7

from statistics import median, mean

def parse_input (file):
    return [int(i) for i in open(file).read().split(",")]

# Caluctate the nth number in the triangular number sequence
def tri(n):
    return n*(n+1)/2

# Simple calculation of Euclidean distance between two points p and q
def dist(p, q):
    return abs(p-q)

# PART 1
#data = parse_input('C:\Code\Advent of Code\\2021\\07\example.txt')
data = parse_input('C:\Code\Advent of Code\\2021\\07\input.txt')

low, high = min(data), max(data)

alignment_point = int(median(data))
fuel = sum([abs(alignment_point - pos) for pos in data])

print(f'Part 1: {fuel}')

# PART 2
# The fuel are calculated using the triangular number sequence
# Formula: nth term = n(n+1)/2
alignment_point = int(mean(data))
fuel = int(min([
    #sum(abs(alignment_point - pos) * (abs(alignment_point - pos) + 1) / 2 for pos in data)
    sum(tri(dist(alignment_point, pos)) for pos in data)
]))


print(f'Part 2: {fuel}')

