# Advent of Code 2021 Day 1 Puzzle 2

#import sys
#input_file = sys.stdin

input_file = open("input_2")

depth_increased = 0
previous_values = []

for line in input_file:
    value = int(line.strip())
    previous_values.insert(0, value)
    if len(previous_values) == 4:
        if sum(previous_values[0:3]) > sum(previous_values[1:4]):
            depth_increased += 1
        previous_values.pop()

print(f"{depth_increased}")        
