# Advent of Code 2021 Day 5
from itertools import chain

def main():
    input_file_name = "test_input"
    input_file_name = "input"

    lines = read_lines_input(input_file_name)
    max_x, max_y = find_extent(lines)
    thermal_map = []
    thermal_map = create_empty_map(thermal_map, max_x, max_y)

    #culled_lines = line_selection(lines)
    culled_lines = lines

    apply_lines_to_map(thermal_map, culled_lines)

    cutoff = 2
    score = score_map(thermal_map, cutoff)

    print(f"Scored at {score}")
    return

def apply_lines_to_map(thermal_map : list[list[int]], lines_to_apply : list) -> None:
    for line in lines_to_apply:
        if line[0][0] == line[1][0]:
            x = line[0][0]
            min_y = min(line[0][1], line[1][1])
            max_y = max(line[0][1], line[1][1]) + 1
            for y in range(min_y, max_y):
                thermal_map[y][x] += 1
        elif line[0][1] == line[1][1]:
            y = line[0][1]
            min_x = min(line[0][0], line[1][0])
            max_x = max(line[0][0], line[1][0]) + 1
            for x in range(min_x,max_x):
                thermal_map[y][x] += 1
        else:
            x1 = line[0][0]
            x2 = line[1][0]
            xdir = -1 if x1 > x2 else 1
            y1 = line[0][1]
            y2 = line[1][1]
            ydir = -1 if y1 > y2 else 1

            for point in zip(range(x1,x2 + xdir, xdir),range(y1,y2 + ydir, ydir)):
                thermal_map[point[1]][point[0]] += 1
    return

def score_map(thermal_map : list[list[int]], cutoff : int) -> int :
    return len([x for x in chain(*thermal_map) if x >= cutoff])

def line_selection(lines : list) -> list:
    # Return only lines where x1==x2 or y1==y2
    return [x for x in lines if (x[0][0] == x[1][0] or x[0][1] == x[1][1])]

def find_extent(lines : list) -> tuple[int,int]:
    max_x = max([x[0][0] for x in lines] + [x[1][0] for x in lines])+1
    max_y = max([x[0][1] for x in lines] + [x[1][1] for x in lines])+1
    
    return max_x, max_y

def create_empty_map(thermal_map : list[list[int]], max_x : int, max_y : int) -> list[list[int]]:
    thermal_map = [[0 for x in range(max_x)] for y in range(max_y)]
    return thermal_map

def read_lines_input(input_file_name : str) -> list:
    lines = []
    with open(input_file_name) as input_file:
        for line_string in input_file:
            line_temp = line_string.strip().split(" -> ")
            line = [[int(x) for x in line_temp[0].split(",")], [int(x) for x in line_temp[1].split(",")]]
            lines.append(line)
    return lines

if __name__ == "__main__":
    main()
