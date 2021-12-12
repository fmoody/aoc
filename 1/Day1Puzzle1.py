# Advent of Code 2021 Day 1 Puzzle 1

#import sys
#input_file = sys.stdin

input_file = open("input")

depth_increased = 0
previous_value = None

for line in input_file:
    value = int(line.strip())
    if previous_value is not None:
        if value > previous_value:
            depth_increased += 1
    previous_value = value

print(f"{depth_increased}")        
