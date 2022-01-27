# Advent of Code 2021 Day 10
from typing import List, Tuple

def main():
    #input_file = "test_input"
    input_file = "input"
    input_subsystem : List[List[str]] = read_input(input_file)

    parser_score : int
    uncorrupted_subsystem : List[List[str]]
    completion_sequences : List[List[str]]
    (parser_score, uncorrupted_subsystem) = uncorrupt_subsystem(input_subsystem)
    completion_sequences = complete_subsystem(uncorrupted_subsystem)
    autocomplete_score = middle_score(score_sequences(completion_sequences))

    print(f"Parser Score        : {parser_score}")
    print(f"Autocompletion Score: {autocomplete_score}")
    return

def middle_score(list_of_scores : List[int]) -> int:
    list_of_scores.sort()

    return list_of_scores[len(list_of_scores)//2]

def score_sequences(completion_sequences : List[List[str]]) -> List[int]:
    list_of_scores : List[int] = []
    for line in completion_sequences:
        list_of_scores.append(score_sequence(line))

    return list_of_scores

def score_sequence(line : List[str]) -> int:
    total_score : int = 0
    for char in line:
        total_score *= 5
        total_score += char_score(char)
    
    return total_score

def char_score(char : str) -> int:
    score : int = 0 
    if char == ')':
        score = 1
    if char == ']':
        score = 2
    if char == '}':
        score = 3
    if char == '>':
        score = 4
    return score

def complete_subsystem(input_subsystem : List[List[str]]) -> List[List[str]]:
    completion_sequences : List[List[str]] = []

    for line in input_subsystem:
        completion_sequences.append(complete_line(line))
    
    return completion_sequences

def complete_line(line : List[str]) -> List[str]:
    completion_sequence : List[str] = []
    mystack : List[str] = []
    for char in line:
        if char == '(' or char == '[' or char == '{' or char == '<' :
            mystack.append(char)
        else:
            current_chunk_type : str = mystack.pop()
            current_chunk_closer = chunk_closer(current_chunk_type)
            while (current_chunk_closer != char):
                completion_sequence.append(current_chunk_closer)
                current_chunk_type = mystack.pop()
    for char in mystack:
        completion_sequence.append(chunk_closer(char))

    completion_sequence.reverse()

    return completion_sequence

def chunk_closer(current_chunk_type : str) -> str:
    chunk_closer : str = ''
    if current_chunk_type == '(':
        chunk_closer = ')'
    if current_chunk_type == '[':
        chunk_closer = ']'
    if current_chunk_type == '{':
        chunk_closer = '}'
    if current_chunk_type == '<':
        chunk_closer = '>'
    return chunk_closer

def uncorrupt_subsystem(input_subsystem : List[List[str]]) -> Tuple[int,List[List[str]]]:
    parser_score = 0
    illegal_char : str = ''
    uncorrupted_subsystem : List[List[str]] = []

    for line in input_subsystem:
        illegal_char = check_line(line)
        if illegal_char:
            if illegal_char == ')':
                parser_score += 3
            if illegal_char == ']':
                parser_score += 57
            if illegal_char == '}':
                parser_score += 1197
            if illegal_char == '>':
                parser_score += 25137
        else:
            uncorrupted_subsystem.append(line)

    return parser_score,uncorrupted_subsystem

def check_line(line : List[str]) -> str:
    mystack : List[str] = []
    eol : str = ''
    for char in line:
        if char == '(' or char == '[' or char == '{' or char == '<' :
            mystack.append(char)
        else:
            current_chunk_type = mystack.pop()
            if  (char == ')' and current_chunk_type != '(') or \
                (char == ']' and current_chunk_type != '[') or \
                (char == '}' and current_chunk_type != '{') or \
                (char == '>' and current_chunk_type != '<') :
                    eol = char
                    break
    return eol

def read_input(input_file_name : str) -> List[List[str]]:
    with open(input_file_name) as input_file:
        input_subsystem = [list(input_line.strip()) for input_line in input_file]
    return input_subsystem

if __name__ == "__main__":
    main()
