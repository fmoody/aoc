# Advent of Code 2021 Day 6

def main():
    input_file_name = "test_input"
    input_file_name = "input"

    target_days = 18
    target_days = 80

    fish_array = read_input(input_file_name)

    for days in range(target_days):
        grow_fish(fish_array)

    fish_count = len(fish_array)
    print(f"Fish count: {fish_count}")

def grow_fish(fish_array : list[int]) -> None:
    time_to_spawn = 6 # 7 days minus 1 for zero-based count
    time_to_start = 2
    for index in range(len(fish_array)):
        if fish_array[index] == 0:
            fish_array[index] = time_to_spawn
            fish_array.append(time_to_spawn + time_to_start)
        else:
            fish_array[index] -= 1

def read_input(input_file_name : str) -> list:
    lines = []
    with open(input_file_name) as input_file:
        fish_array = [int(x) for x in input_file.readline().strip().split(",")]
    return fish_array

if __name__ == "__main__":
    main()
