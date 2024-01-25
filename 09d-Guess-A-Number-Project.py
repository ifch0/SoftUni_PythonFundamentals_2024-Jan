import random

target_number = random.randint(1, 100)

end_of_game = False

while end_of_game == False:
    user_input = input('Guess the number (1-100) or Quit (0): ')

    if not user_input.isdigit():
        print(f'Enter number!')
    else:
        if int(user_input) == 0:
            end_of_game = True
        elif int(user_input) == target_number:
            print(f'That\'s correct! The correct number is {user_input}')
            end_of_game = True
        elif int(user_input) > target_number:
            print(f'Too high!')
        elif int(user_input) < target_number:
            print(f'Too low!')
