# Advent of Code 2021 Day 11
from typing import List, Tuple

def main():
    input_file = "test_input"
    #input_file = "input"
    octopus_energy : List[List[int]]
    octopus_energy = read_input(input_file)

    steps : int = 100
    total_flashes : int = 0
    for step in range(steps):
        flashes_this_step, octopus_energy = simulate_octopus_step(octopus_energy)
        print(f"Step {step} Flashes: {flashes_this_step}")
        total_flashes += flashes_this_step

    print(f"Total Flashes: {total_flashes}")

    return

def simulate_octopus_step(octopus_energy : List[List[int]]) -> Tuple[int,List[List[int]]]:
    flashes_this_step : int = 0
# Do the actual stuff
    return flashes_this_step, octopus_energy

def read_input(input_file_name : str) -> List[List[int]]:
    octopus_energy : List[List[int]]
    with open(input_file_name) as input_file:
        octopus_energy = [list(map(lambda x : int(x), input_line.strip())) for input_line in input_file]

    return octopus_energy

if __name__ == "__main__":
    main()
