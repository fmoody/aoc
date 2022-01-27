# Advent of Code 2021 Day 8

from typing import List, Dict, Tuple

def main():
    #input_file_name = "test_input"
    input_file_name = "input"

    notes = read_input(input_file_name)
    # Part 1, easy count
    # counts = count_easy(notes)

    # print(f"Counts returned: {counts}")
    sum_of_values = 0

    for x in notes:
        conversion_table = create_conversion_table(x[0])
        sum_of_values += convert_output(x[1], conversion_table)
    
    print(f"Sum of the values is: {sum_of_values}")
    
    return

def convert_output(output_list : List[str], conversion_table: Dict[str,str]) -> int:
    print(f"Value to convert: {output_list}")
    converted_output_list = [conversion_table[''.join(sorted(x))] for x in output_list]
    output_string = ''.join(converted_output_list)
    return int(output_string)

def create_conversion_table(patterns : List[str]) -> Dict[str, str]:
    conversion_table : Dict[str, str] = {}

    # Step 1: Easy to find patterns for 1, 4, 7, 8 based on length
    pattern_1 = [x for x in patterns if len(x) == 2][0]
    conversion_table[''.join(sorted(pattern_1))] = '1'
    pattern_4 = [x for x in patterns if len(x) == 4][0]
    conversion_table[''.join(sorted(pattern_4))] = '4'
    pattern_7 = [x for x in patterns if len(x) == 3][0]
    conversion_table[''.join(sorted(pattern_7))] = '7'
    pattern_8 = [x for x in patterns if len(x) == 7][0]
    conversion_table[''.join(sorted(pattern_8))] = '8'

    # Step 2: Look for patterns that can be deduced from existing patterns....

    # 6 
    pattern_6 = [x for x in patterns if len(x) == 6 and len(set(x)-set(pattern_1)) == 5][0]
    conversion_table[''.join(sorted(pattern_6))] = '6'

    # 5
    pattern_5 = [x for x in patterns if len(x) == 5 and len(set(x) - set(pattern_6)) == 0][0]
    conversion_table[''.join(sorted(pattern_5))] = '5'
    # 2
    pattern_2 = [x for x in patterns if len(x) == 5 and len(set(x) - set(pattern_5)) == 2][0]
    conversion_table[''.join(sorted(pattern_2))] = '2'
    # 3
    pattern_3 = [x for x in patterns if len(x) == 5 and len(set(x)-set(pattern_5)) == 1][0]
    conversion_table[''.join(sorted(pattern_3))] = '3'

    # 0 
    pattern_0 = [x for x in patterns if x != pattern_6 and len(x) == 6 and len(set(x) - set(pattern_4)) == 3][0]
    conversion_table[''.join(sorted(pattern_0))] = '0'
    # 9 
    pattern_9 = [x for x in patterns if x != pattern_6 and len(x) == 6 and len(set(x) - set(pattern_4)) == 2][0]
    conversion_table[''.join(sorted(pattern_9))] = '9'

    return conversion_table

def count_easy(notes : List[Tuple[List[str],List[str]]]) -> int:
    counts = 0
    for note in notes:
        note_lengths = [len(pattern) for pattern in note[1]]
        for char_len in [2,4,3,7]:
            counts += note_lengths.count(char_len)
    return counts


def read_input(input_file_name : str) -> List[Tuple[List[str],List[str]]]:
    with open(input_file_name) as input_file:
        notes = [input_line.split("|") for input_line in input_file]
        #notes = [["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab","cdfeb fcadb cdfeb cdbaf"]]
        processed_notes : List[Tuple[List[str],List[str]]] = []
        for index in range(len(notes)):
            # notes[index][0]=notes[index][0].strip().split()
            # notes[index][1]=notes[index][1].strip().split()
            processed_notes.append((notes[index][0].strip().split(),notes[index][1].strip().split()))

    return processed_notes

if __name__ == "__main__":
    main()
