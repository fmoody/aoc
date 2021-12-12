# Advent of Code 2021 Day 6
from functools import cache 

def main():
    #input_file_name = "test_input"
    input_file_name = "input"

    target_days = 18
    target_days = 80
    #target_days = 180
    target_days = 256

    fish_array = read_input(input_file_name)

    #fish_count = len(grow_fishes2(fish_array, target_days))
    #fish_count = grow_fishes3(fish_array, target_days)
    fish_count = grow_fishes4(fish_array, target_days)

    print(f"Fish count: {fish_count}")

def grow_fishes(fish_array : list[int], target_days : int) -> list[int]:
    time_to_spawn = 6 # 7 days minus 1 for zero-based count
    time_to_start = 2
    for day in range(target_days):
        print(f"Day {day}")
        for index in range(len(fish_array)):
            if fish_array[index] == 0:
                fish_array[index] = time_to_spawn
                fish_array.append(time_to_spawn + time_to_start)
            else:
                fish_array[index] -= 1
    return fish_array

def grow_fishes2(fish_array : list[int], target_days : int) -> list[int]: # 14.0 @ 180
    time_to_spawn = 6 # 7 days minus 1 for zero-based count
    time_to_start = 2
    for day in range(target_days):
        fish_array.sort()
        spawn_count = fish_array.count(0)
        del fish_array[:spawn_count]
        fish_array = [fish-1 for fish in fish_array]
        fish_array += [time_to_spawn]*spawn_count # Old fish
        fish_array += [time_to_spawn+time_to_start]*spawn_count # New fish
    return fish_array

def grow_fishes3(fish_array : list[int], target_days : int) -> int: # 11.2 @ 180
    time_to_spawn = 6 # 7 days minus 1 for zero-based count
    time_to_start = 2
    fish_count = 0
    for fish in fish_array:
        fish_count += grow_fish(fish, target_days, time_to_spawn,time_to_start)
    return fish_count

@cache
def grow_fish(fish : int, target_days : int, time_to_spawn : int,time_to_start : int):
    fish_array = [fish]
    for day in range(target_days):
        fish_array.sort()
        spawn_count = fish_array.count(0)
        del fish_array[:spawn_count]
        fish_array = [fish-1 for fish in fish_array]
        fish_array += [time_to_spawn]*spawn_count # Old fish
        fish_array += [time_to_spawn+time_to_start]*spawn_count # New fish
    return len(fish_array)

def grow_fishes4(fish_array : list[int], target_days : int) -> int:
    time_to_spawn = 7
    time_to_start = 2
    spawn_slots = time_to_spawn+time_to_start
    # Prepopulate the existing fish
    fish_spawn_lots = [0 for x in range(spawn_slots)]
    for fish in fish_array:
        fish_spawn_lots[fish] += 1
    
    # For each day
    for day in range(target_days):
        # Calculate the number of spawning fish 
        spawn_count = fish_spawn_lots[0]
        # Move all values down one slot
        for slot in range(len(fish_spawn_lots)):
            if slot < len(fish_spawn_lots) -1:
                fish_spawn_lots[slot] = fish_spawn_lots[slot+1]
        # Add the spawn count for both spawning and spawned
        fish_spawn_lots[time_to_spawn - 1] += spawn_count
        fish_spawn_lots[time_to_spawn + time_to_start -1] = spawn_count
    return sum(fish_spawn_lots)

def read_input(input_file_name : str) -> list:
    with open(input_file_name) as input_file:
        fish_array = [int(x) for x in input_file.readline().strip().split(",")]
    return fish_array

if __name__ == "__main__":
    main()
