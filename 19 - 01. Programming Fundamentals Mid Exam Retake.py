# 01. Computer Store

end_of_order = False
total_price = 0
discount_perc = 1
cat = 0

while end_of_order == False:
    user_input = input()

    if user_input == 'special':
        discount_perc = 0.9
        end_of_order = True
    elif user_input == 'regular':
        end_of_order = True
    else:
        try:
            item_price = float(user_input)
            if item_price <= 0:
                print(f'Invalid price!')
            else:
                total_price += item_price
        except:
            ValueError

vat = total_price * 0.2
grand_total = (total_price + vat) * discount_perc

if end_of_order == True and total_price != 0:
    print(f'Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {vat:.2f}$')
    print(f'-----------')
    print(f'Total price: {grand_total:.2f}$')
else:
    print(f'Invalid order!')

# 02. The Lift

people_queue = int(input())
lift_cars = [int(x) for x in input().split(' ')]
lift_car_capacity = 4
lift_max_capacity = len(lift_cars) * lift_car_capacity

lift_full = False
no_more_people = False

for car in range(len(lift_cars)):
    while lift_cars[car] < 4 and people_queue > 0:
        lift_cars[car] += 1
        people_queue -= 1
        if sum(lift_cars) == lift_max_capacity:
            lift_full = True
        if people_queue == 0:
            no_more_people = True

if no_more_people and not lift_full:
    print(f'The lift has empty spots!')
elif lift_full and not no_more_people:
    print(f'There isn\'t enough space! {people_queue} people in a queue!')

print(*lift_cars)

# 03. Memory Game

elements_sequence = input().split(' ')

def is_valid(ind_1, ind_2):
    if ind_1 == ind_2 or ind_1 < 0 or ind_2 < 0 or ind_1 > len(elements_sequence) or ind_2 > len(elements_sequence):
        return False
    else:
        return True

def found_matching(ind_1, ind_2):
    if elements_sequence[ind_1] == elements_sequence[ind_2]:
        return True
    else:
        return False

def remove_elements(ind_1, ind_2):
    print(f'Congrats! You have found matching elements - {elements_sequence[split_command[ind_1]]}!')
    if ind_1 > ind_2:
        elements_sequence.pop(ind_1)
        elements_sequence.pop(ind_2)
    else:
        elements_sequence.pop(ind_2)
        elements_sequence.pop(ind_1)

def invalid_input():
    print(f'Invalid input! Adding additional elements to the board')
    mid_point = int(len(elements_sequence)/2)
    new_element = '-' + str(moves_counter) + 'a'
    elements_sequence.insert(mid_point, new_element)
    elements_sequence.insert(mid_point, new_element)

moves_counter = 0
won = False
end_of_game = False
while end_of_game == False and won == False:
    input_command = input()
    if input_command == 'end':
        end_of_game = True
    else:
        try:
            split_command = list(map(int, input_command.split(' ')))
            moves_counter += 1
            if is_valid(*split_command):
                if found_matching(*split_command):
                    remove_elements(*split_command)
                else:
                    print(f'Try again!')
            else:
                invalid_input()
            if len(elements_sequence) == 0:
                won = True
        except:
            invalid_input()

if won == True:
    print(f'You have won in {moves_counter} turns!')
else:
    print(f'Sorry you lose :(')
    print(*elements_sequence)
