# Advent of Code 2021 Day 3 Puzzle 1&2

from functools import reduce

def main():
    
    #input_file_name = "test_input"
    input_file_name = "input"

    with open(input_file_name) as input_file: input_data = [[item for item in map(lambda x: int(x), list(line.strip()))] for line in input_file]

    most_common_bits, least_common_bits, counting_bits = bit_freq(input_data, 'neutral')
    gamma = bits_to_int(most_common_bits)
    epsilon = bits_to_int(least_common_bits)

    oxygen_generator_rating = bits_to_int(select_rating(input_data, 'O2'))
    co2_scrubber_rating = bits_to_int(select_rating(input_data, 'CO2'))

    print(f"Gamma: {gamma}")
    print(f"Epsilon: {epsilon}")
    print(f"Power consumption: {gamma*epsilon}")

    print(f"O2 Generator: {oxygen_generator_rating}")
    print(f"CO2 Scrubber Rating: {co2_scrubber_rating}")
    print(f"Life Support Rating: {oxygen_generator_rating*co2_scrubber_rating}")

    return

def bits_to_int(bit_list):
    return reduce(lambda accum, bit: (accum << 1)+bit, bit_list)

def select_rating(input_data, choice):
    position = 0
    working_set = input_data
    while(len(working_set)>1):
        most_common_bits, least_common_bits, counting_bits = bit_freq(working_set,choice)
        working_set = [item for item in working_set if item[position] == (most_common_bits[position] if choice == 'O2' else least_common_bits[position]) ]
        position += 1
    return working_set[0]

def bit_freq(bit_list, choice):
    half_count = len(bit_list)/2
    counting_bits = list(map(sum,list(zip(*bit_list))))
    most_common_bits = list(map(lambda x: 1 if x >= half_count else 0,counting_bits))
    least_common_bits = list(map(lambda x: 0 if x else 1, most_common_bits))
    return most_common_bits, least_common_bits,counting_bits

if __name__ == "__main__":
    main()