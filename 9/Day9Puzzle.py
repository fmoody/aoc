# Advent of Code 2021 Day 9
from typing import List, Tuple
from functools import reduce

def main():
    input_file = "test_input"
    input_file = "input"
    height_map = read_input(input_file)

    print("Working with map:")
    print(f"{height_map}")

    max_x = len(height_map)
    max_y = len(height_map[0]) # assuming a square map

    sum_of_risk : int = 0
    list_of_low_points : List[Tuple[int,int]] = []
    for x in range(max_x):
        for y in range(max_y):
            testing = is_low_point(height_map,x,y, max_x, max_y)
            if testing:
                print(f"x: {x} y: {y} height: {height_map[x][y]}")
                sum_of_risk += 1+height_map[x][y]
                list_of_low_points.append((x,y))

    global visit_list
    visit_list = []

    basin_sizes = [calc_basin_size(x,y,height_map) for (x,y) in list_of_low_points]

    basin_sizes.sort(reverse=True)

    big_basin_calc = reduce(lambda x,y : x * y, basin_sizes[:3])
    print(f"Assessed and summed risk: {sum_of_risk}")
    print(f"Basin sizes: {basin_sizes}")
    print(f"Basin calculation: {big_basin_calc}")

    return

def calc_basin_size(x: int, y : int, height_map : List[List[int]]) -> int:
    global visit_list

    if (x,y) not in visit_list:
        visit_list.append((x,y))
        basin_left    : int = 0 if y == 0 or height_map[x][y-1] == 9 else calc_basin_size(x,y-1,height_map)
        basin_right  : int = 0 if y+1 == len(height_map[x]) or height_map[x][y+1] == 9 else calc_basin_size(x,y+1,height_map)
        basin_up  : int = 0 if x == 0 or height_map[x-1][y] == 9 else calc_basin_size(x-1,y,height_map)
        basin_down : int = 0 if x+1 == len(height_map) or height_map[x+1][y] == 9 else calc_basin_size(x+1,y,height_map)
        return 1 + basin_up + basin_down + basin_left + basin_right
    else:
        return 0

def is_low_point(height_map : List[List[int]], x : int, y : int, max_x : int, max_y : int) -> bool:
    x_minus = (x != 0 and height_map[x-1][y] <= height_map[x][y])
    x_positive = (x + 1 < max_x and height_map[x+1][y] <= height_map[x][y])
    y_minus = (y != 0 and height_map[x][y-1] <= height_map[x][y])
    y_positive = (y + 1 < max_y and height_map[x][y+1] <= height_map[x][y])

    return False if x_minus or x_positive or y_minus or y_positive else True

def read_input(input_file_name : str) -> List[List[int]]:
    with open(input_file_name) as input_file:
        height_map = [list(map(lambda x: int(x), list(input_line.strip()))) for input_line in input_file]
    return height_map

if __name__ == "__main__":
    main()
