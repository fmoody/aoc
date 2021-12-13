# Advent of Code 2021 Day 8

def main():
    #input_file_name = "test_input"
    input_file_name = "input"

    notes = read_input(input_file_name)
    counts = 0
    for note in notes:
        print(f"Note: {notes[1]}")
        note_lengths = [len(pattern) for pattern in note[1]]
        for char_len in [2,4,3,7]:
            counts += note_lengths.count(char_len)
            print(f"{char_len} : {note_lengths.count(char_len)}")
        print(f"Progress count: {counts}")

    print(f"Counts returned: {counts}")
    return


def read_input(input_file_name : str):
    with open(input_file_name) as input_file:
        notes = [input_line.split("|") for input_line in input_file]
        for index in range(len(notes)):
            notes[index][0]=notes[index][0].strip().split()
            notes[index][1]=notes[index][1].strip().split()
    return notes

if __name__ == "__main__":
    main()
