# Advent of Code 2021 Day 2 Puzzle 1

#import sys
#input_file = sys.stdin

input_file = open("input")

distance = 0
depth = 0
aim = 0

for line in input_file:
    command, value_str = line.strip().split(" ")
    value = int(value_str)
    if command == "forward" :
        distance += value
        depth += aim*value
    elif command == "up":
        aim -= value
    elif command == "down":
        aim += value
    else:
        print(f"Unknown command {command} in {line}")

print(f"{distance*depth}")
