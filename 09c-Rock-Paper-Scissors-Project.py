import random

user_input = input('Choose [r]ock, [p]aper or [s]cissors: ')

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = ''
computer_move = ''

if user_input == 'r':
    player_move = rock
elif user_input == 'p':
    player_move = paper
elif user_input == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid Input. Try again...')

computer_choice = random.randint(1, 3)

if computer_choice == 1:
    computer_move = rock
elif computer_choice == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f'The computer chose {computer_move}.')

if computer_move == player_move:
    print(f'Draw!')
elif computer_move == rock:
    if player_move == paper:
        print(f'You win!')
    elif player_move == scissors:
        print(f'You lose!')
elif computer_move == paper:
    if player_move == rock:
        print(f'You lose!')
    elif player_move == scissors:
        print(f'You win!')
elif computer_move == scissors:
    if player_move == rock:
        print(f'You win!')
    elif player_move == paper:
        print(f'You lose!')

