# Advent of Code 2021 Day 4 Puzzle 1
from itertools import chain

def main():
    input_file_name = "test_input"
    input_file_name = "input"

    number_draw, bingo_cards = read_input(input_file_name)

    win_first = True
    win_first = False
    winning_cards = []

    drawn_numbers = []
    cards_state = create_cards_state(len(bingo_cards))

    for number_drawn in number_draw:
        update_cards_state(cards_state, bingo_cards, number_drawn)
        new_winning_cards = win_check_cards(cards_state)
        if len(new_winning_cards) != 0:
            winning_cards.append(new_winning_cards)
            all_cards_won = len(set(chain(*winning_cards))) == len(bingo_cards)
            if win_first or all_cards_won:
                break

    # win_first will start out with only one card in one set of wins in the winning cards list.  !win_first will need culling by find_last_win
    if win_first:
        winning_card = winning_cards.pop().pop()
    else:
        winning_card = find_last_win(winning_cards)

    winning_score = calculate_score(bingo_cards[winning_card], cards_state[winning_card], number_drawn)
    print(f"Winning Score is {winning_score}")

    return

def find_last_win(winning_cards):
    flat_wins = list(chain(*winning_cards))
    winning_cards_set = set(flat_wins)
    for win in flat_wins:
        if win in winning_cards_set:
            winning_cards_set.remove(win)
            if len(winning_cards_set) == 1:
                break
    return winning_cards_set.pop()

def calculate_score(bingo_card, card_state, number_drawn):
    board_states = list(chain(*card_state))
    board_values = list(chain(*bingo_card))
    board_scores = [int(board_values[index]) if board_states[index] == False else 0 for index in range(25)]
    board_sum = sum(board_scores)
    return board_sum * int(number_drawn)

def win_check_cards(cards_state):
    winning_cards = []
    for card_number in range(len(cards_state)):
        if win_check_card(cards_state[card_number]) == True:
            winning_cards.append(card_number)
    return winning_cards

def win_check_card(card_state):
    # Check rows first
    for row_number in range(5):
        if False not in card_state[row_number]:
            return True

    # Check columns next
    for column_number in range(5):
        if False not in map(lambda x: x[column_number], card_state):
            return True

    # Otherwise didn't win
    return False

def update_cards_state(cards_state, bingo_cards, number_drawn):
    for card_number in range(len(bingo_cards)):
        for row_number in range(5):
            if number_drawn in bingo_cards[card_number][row_number]:
                position = bingo_cards[card_number][row_number].index(number_drawn)
                cards_state[card_number][row_number][position] = True

                while(number_drawn in bingo_cards[card_number][row_number][position+1:]):
                    position = bingo_cards[card_number][row_number].index(number_drawn, position+1)
                    cards_state[card_number][row_number][position] = True

    return cards_state

def create_cards_state(number_of_cards):
    cards_state = []
    for count in range(number_of_cards):
        card_state = [[False for x in range(5)] for y in range(5)]
        cards_state.append(card_state)
    return cards_state

def read_input(input_file_name):
    with open(input_file_name, "r") as input_file:
        number_draw = input_file.readline().strip().split(",")

        bingo_cards = []
        bingo_cards_input = list(input_file)
        
    while(len(bingo_cards_input) > 0):
        bingo_cards_input.pop(0) # Empty Space
        temp_bingo_card = []
        temp_bingo_card.append(bingo_cards_input.pop(0).strip().split())
        temp_bingo_card.append(bingo_cards_input.pop(0).strip().split())
        temp_bingo_card.append(bingo_cards_input.pop(0).strip().split())
        temp_bingo_card.append(bingo_cards_input.pop(0).strip().split())
        temp_bingo_card.append(bingo_cards_input.pop(0).strip().split())
        bingo_cards.append(temp_bingo_card)
    
    return number_draw, bingo_cards

if __name__ == "__main__":
    main()
