with open('input.txt', 'r') as f:
    data = [int(value) for value in f.readlines()]

# PART 1 #
def part1(input):
    return sum(current > prev for prev, current in zip(input, input[1:]))

# PART 2 #
def part2(input):
  return sum(current > prev for prev, current in zip(input, input[3:]))

print(part1(data))
print(part2(data))

# PART 1 #
prev = -1
count = 0

for num in data:
    if prev < num and prev != -1:
        count += 1
    
    prev = num

print("Result: ", count)
