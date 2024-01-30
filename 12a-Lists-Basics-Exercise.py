# 01. Invert Values

input_string = input()

split_string = input_string.split()
opposite_string = []

for i in range(len(split_string)):
    current_value = int(split_string[i])
    current_value *= -1
    opposite_string.append(current_value)

print(opposite_string)

# 02. Multiples List

starting_number = int(input())
counter = int(input())

full_list = []

for i in range(1, counter + 1):
    full_list.append(starting_number * i)

print(full_list)

# 03. Football Cards

input_string = input()

team_a_players = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
team_b_players = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

cards_list = input_string.split()

for card in range(len(cards_list)):
    split_card = cards_list[card].split('-')
    team = split_card[0]
    player_position = int(split_card[1])
    if team == 'A':
        team_a_players[player_position] = 0
    elif team == 'B':
        team_b_players[player_position] = 0
    else:
        pass

print(f'Team A - {sum(team_a_players)}; Team B - {sum(team_b_players)}')

if sum(team_a_players) < 7 or sum(team_b_players) < 7:
    print(f'Game was terminated')

# 03. Football Cards (80/100 - to be continue)

input_string = input()

team_a_players = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
team_b_players = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

cards_list = input_string.split(' ')
not_enough_players = False

for i in range(len(cards_list)):
    split_card = cards_list[i].split('-')
    if len(split_card) != 2:
        continue
    team = split_card[0]
    try:
        player_position = int(split_card[1]) - 1
        if player_position < 0 or player_position > 12:
            continue
        if team == 'A':
            team_a_players[player_position] = 0
        elif team == 'B':
            team_b_players[player_position] = 0
        else:
            pass
    except:
        ValueError

    if sum(team_a_players) < 7 or sum(team_b_players) < 7:
        not_enough_players = True
        break

print(f'Team A - {sum(team_a_players)}; Team B - {sum(team_b_players)}')

if not_enough_players == True:
    print(f'Game was terminated')

# 04. Number Beggars

input_string = input()
count_of_beggars = int(input())

split_string = input_string.split(', ')

personal_earnings = []
for beggar in range(count_of_beggars):
    personal_earnings.append(0)

beggar_turn = 0

for i in range(len(split_string)):
    personal_earnings[beggar_turn] += int(split_string[i])

    beggar_turn += 1
    if beggar_turn == count_of_beggars:
        beggar_turn = 0

print(personal_earnings)

# 05. Faro Shuffle

input_string = input()
qty_faro_shuffle = int(input())

listed_string = input_string.split(' ')
length = int(len(listed_string)/2)

substring_a = []
substring_b = []
shuffled_string = listed_string

for shuffle in range(qty_faro_shuffle):
    substring_a = []
    substring_b = []
    for j in range(length):
        substring_a.append(shuffled_string[j])
        substring_b.append(shuffled_string[j+length])

    shuffled_string = []

    for i in range(length):
        shuffled_string.append(substring_a[i])
        shuffled_string.append(substring_b[i])

print(shuffled_string)

# 06. Survival of the Biggest

from math import inf

input_string = input()
digits_to_remove = int(input())

input_list = input_string.split(' ')
input_int_list = [int(x) for x in input_list]
        
for i in range(digits_to_remove):
    min_value = inf
    position = 0
    for j in range(len(input_int_list)):
        if input_int_list[j] < min_value:
            min_value = input_int_list[j]
            position = j
    input_int_list.pop(position)

print(*input_int_list, sep=', ')

# 
