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

# 07. Easter Gifts

string_input = input()

gift_list = string_input.split(' ')
output_list = []
no_money = False


def OutOfStock(gift):
    for i in range(len(gift_list)):
        if gift_list[i] == gift:
            gift_list[i] = 'None'

def Required(gift, index):
    if 0 <= index < len(gift_list):
        gift_list[index] = gift

def JustInCase(gift):
    gift_list.pop()
    gift_list.append(gift)

while no_money == False:
    user_command = input()

    command_list = user_command.split(' ')

    if command_list[0] == 'No' and command_list[1] == 'Money':
        no_money = True
    elif command_list[0] == 'OutOfStock':
        OutOfStock(command_list[1])
    elif command_list[0] == 'Required':
        Required(command_list[1], int(command_list[2]))
    elif command_list[0] == 'JustInCase':
        JustInCase(command_list[1])
    else:
        pass

for gift in gift_list:
    if gift != 'None':
        output_list.append(gift)
print(*output_list, sep=' ')

# 08. Seize the Fire 

fires_and_cells_input = input()
available_water = int(input())
cells_done = []
firs_and_cells_list = fires_and_cells_input.split('#')

for i in firs_and_cells_list:
    fire_cell = i.split(' = ')

    if (fire_cell[0] == 'High' and 81 <= int(fire_cell[1]) <=125) or (fire_cell[0] == 'Medium' and 51 <= int(fire_cell[1]) <=80) or (fire_cell[0] == 'Low' and 1 <= int(fire_cell[1]) <=50):
        if available_water >= int(fire_cell[1]):
            available_water -= int(fire_cell[1])
            cells_done.append(int(fire_cell[1]))
    else:
        pass

print(f'Cells:')
for cell in cells_done:
    print(f'- {cell}')

total_fire = sum(cells_done)
effort = total_fire * 0.25

print(f'Effort: {effort:0.2f}')
print(f'Total Fire: {total_fire}')

# 09. Hello, France

items_input = input()
initial_budget = float(input())
ticket_price = 150

available_budget = initial_budget

bought_items = []

items_list = items_input.split('|')

for item in items_list:
    item_properties = item.split('->')

    if (item_properties[0] == 'Clothes' and float(item_properties[1]) <= 50) or (item_properties[0] == 'Shoes' and float(item_properties[1]) <= 35) or (item_properties[0] == 'Accessories' and float(item_properties[1]) <= 20.50):
        if available_budget >= float(item_properties[1]):
            available_budget -= float(item_properties[1])
            bought_items.append(float(item_properties[1]))

for i in range(len(bought_items)):
    bought_items[i] *= 1.4
    bought_items[i] = round(bought_items[i], 2)

for new_price in bought_items:
    print(f'{new_price:0.2f} ', end='')
print()

available_budget += sum(bought_items)
profit = available_budget - initial_budget

print(f'Profit: {profit:0.2f}')

if available_budget >= ticket_price:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')


# 10. Bread Factory

events_input = input()

events = events_input.split('|')

available_energy = 100
current_coins = 100

closed = False

def rest(added_energy):
    global available_energy
    energy_gap = 100 - available_energy
    if added_energy <= energy_gap:
        available_energy += added_energy
        print(f'You gained {added_energy} energy.')
    else:
        available_energy += energy_gap
        print(f'You gained {energy_gap} energy.')
    print(f'Current energy: {available_energy}.')

def order(coins):
    global available_energy
    global current_coins
    if available_energy >= 30:
        available_energy -= 30
        current_coins += coins
        print(f'You earned {coins} coins.')
    else:
        available_energy += 50
        print(f'You had to rest!')

def ingredients(ingredient, coins):
    global current_coins
    global closed
    if current_coins >= coins:
        current_coins -= coins
        print(f'You bought {ingredient}.')
    else:
        print(f'Closed! Cannot afford {ingredient}.')
        closed = True

for event in events:
    event_details = event.split('-')

    if event_details[0] == 'rest':
        rest(int(event_details[1]))
    elif event_details[0] == 'order':
        order(int(event_details[1]))
    else:
        ingredients(event_details[0], int(event_details[1]))

    if closed == True:
        break

if closed != True:
    print(f'Day completed!')
    print(f'Coins: {current_coins}')
    print(f'Energy: {available_energy}')
