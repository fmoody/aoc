# Advent of Code 2021 Day 6
from functools import cache 

def main():
    #input_file_name = "test_input"
    input_file_name = "input"
    
    crab_positions = read_input(input_file_name)

    minimal_fuel : int = None

    for index in range(min(crab_positions), max(crab_positions)+1):
        fuel = sum([calc_fuel_cost(pos, index) for pos in crab_positions])
        if not minimal_fuel or fuel < minimal_fuel:
            minimal_position = index
            minimal_fuel = fuel

    print(f"Minimum fuel use: {minimal_fuel}")

@cache
def calc_fuel_cost(pos : int, index : int) -> int:
    #return abs(pos - index)
    return sum(range(abs(pos-index)+1))

def read_input(input_file_name : str) -> list:
    with open(input_file_name) as input_file:
        lines = [int(x) for x in input_file.readline().strip().split(",")]
    return lines

if __name__ == "__main__":
    main()
