# --- Day 6: Lanternfish ---
# https://adventofcode.com/2021/day/6

import time

def parse_input (file):
    with open(file, 'r') as f:
        return f.read()


def simulate_lanternfish(fishes: str, days: int):
    lanternfish = [int(i) for i in fishes.split(',')]
    state = [0] * 9     # Create array holding each state - We are using 9 stages as, 0 is a valid state - 9 states in total.

    # Conut the number of fish in each state
    for fish in lanternfish:
        state[fish] += 1    # Add a lanternfish to it's state, in the state array
    
    # Simulate Lanternfish Growth for x days
    for _ in range(days):
        state_zero = state[0]   # Store the current number of lanternfish in state 0

        # Move the number of lanternfish for each state to the previous state (from 0 > 8) so state 1 = state 2, state 2 = state 3  
        for i in range(0, 8):   # Process stage 0 > 7
            state[i] = state[i+1]   # Assign the value of the stage before to the current state
        
        # Reset cycel for stage 0 lanternfish
        state[6] += state_zero  # Add all lanternfish from stage 0 to stage 6 (Cycel reset)

        # Add new lanternfish made in stage 0 (One lanternfish, make one new lanternfish)
        state[8] = state_zero   # Add the same amount of lanternfish to state 8 as there was in stage zero (New lanternfish)        
    
    # Sum the total amount of lanternfish
    return(sum(state))

data = parse_input('C:\Code\Advent of Code\\2021\\06\input.txt')


print('--- PART 1 ---')
time_start = time.perf_counter()
print(f'Result: {simulate_lanternfish(data,80)}')
time_end = time.perf_counter()
print(f'Elapsed time: {time_end - time_start:0.5f} secs.')

print('--- PART 2 ---')
time_start = time.perf_counter()
print(f'Result: {simulate_lanternfish(data,256)}')
time_end = time.perf_counter()
print(f'Elapsed time: {time_end - time_start:0.5f} secs.') 