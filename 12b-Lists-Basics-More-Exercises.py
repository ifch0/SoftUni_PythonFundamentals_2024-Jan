# 01. Zeros to Back

input_string = input()

separated_list = [int(x) for x in input_string.split(', ')]
zero_counter = 0
output_list = []

for i in range(len(separated_list)):
    if separated_list[i] == 0:
        zero_counter += 1
    else:
        output_list.append(separated_list[i])

for i in range(zero_counter):
    output_list.append(0)

print(output_list)

input_string = input()

separated_list = [int(x) for x in input_string.split(', ')]

for i in range(len(separated_list)):
    if separated_list[i] == 0:
        separated_list.pop(i)
        separated_list.append(0)

print(separated_list)

# 02. Messaging

input_numbers = input()
input_string = input()

split_input_numbers = [int(x) for x in input_numbers.split(' ')]
output_string = ''
split_input_string = []

for i in range(len(input_string)):
    split_input_string.append(input_string[i])

for i in range(len(split_input_numbers)):
    character_index = 0
    for digit in str(split_input_numbers[i]):
        character_index += int(digit)

    if character_index >= len(split_input_string):
        character_index -= len(split_input_string)

    output_string += split_input_string.pop(character_index)

print(output_string)

# 03. Car Race

input_string = input()

forward_list = [int(x) for x in input_string.split(' ')]
backward_list = forward_list[::-1]

steps_per_car = int((len(forward_list) - 1) / 2)

right_car_time = 0
left_car_time = 0
winner = ''
winner_time = 0

for step in range(steps_per_car):
    if forward_list[step] == 0:
        left_car_time *= 0.8
    else:
        left_car_time += forward_list[step]

    if backward_list[step] == 0:
        right_car_time *= 0.8
    else:
        right_car_time += backward_list[step]

if right_car_time < left_car_time:
    winner = 'right'
    winner_time = right_car_time
else:
    winner = 'left'
    winner_time = left_car_time

print(f'The winner is {winner} with total time: {winner_time:0.1f}')

# 04. Josephus Permutation

input_string = input()
skip_step = int(input())

input_list = [int(x) for x in input_string.split(' ')]
output_list = []
current_position = 0

def counter(current_position, total):
    for j in range(skip_step):
        current_position += 1
        if current_position >= total:
            current_position = 0
    return current_position

for i in range(len(input_list)):
    current_position = counter(current_position -1 , len(input_list))

    output_list.append(input_list[current_position])
    input_list.pop(current_position)

output_string = ','.join(map(str, output_list))
print(f'[{output_string}]')

# 05. Tic-Tac-Toe

line_a = input()
line_b = input()
line_c = input()

output = 'Draw!'

list_a = [int(x) for x in line_a.split(' ') ]
list_b = [int(x) for x in line_b.split(' ') ]
list_c = [int(x) for x in line_c.split(' ') ]

matrix = [list_a, list_b, list_c]

for row in range(3):
    if matrix[row][0] == matrix[row][1] == matrix[row][2] == 1:
        output = 'First player won'
    elif matrix[row][0] == matrix[row][1] == matrix[row][2] == 2:
        output = 'Second player won'

for column in range(3):
    if matrix[0][column] == matrix[1][column] == matrix[2][column] == 1:
        output = 'First player won'
    elif matrix[0][column] == matrix[1][column] == matrix[2][column] == 2:
        output = 'Second player won'

if matrix[0][0] == matrix[1][1] == matrix[2][2] == 1:
    output = 'First player won'

if matrix[0][0] == matrix[1][1] == matrix[2][2] == 2:
    output = 'Second player won'

if matrix[2][0] == matrix[1][1] == matrix[0][2] == 1:
    output = 'First player won'

if matrix[2][0] == matrix[1][1] == matrix[0][2] == 2:
    output = 'Second player won'

print(output)

# 06. List Manipulator
from math import inf

string_input = input()

list_input = [int(x) for x in string_input.split(' ')]

end = False

def exchange(index):
    temp_list = []
    if 0 <= index < len(list_input):
        for i in range(index + 1, len(list_input)):
            temp_list.append(list_input[i])
        for j in range(0, index + 1):
            temp_list.append(list_input[j])
        return temp_list
    else:
        print('Invalid index')
        return list_input

def max_even_odd(even_odd):
    max = -inf
    max_index = 0
    for i in range(len(list_input)):
        if list_input[i] >= max and list_input[i] % 2 == 0 and even_odd == 'even':
            max = list_input[i]
            max_index = i
        elif list_input[i] >= max and list_input[i] % 2 != 0 and even_odd == 'odd':
            max = list_input[i]
            max_index = i
        else:
            pass

    if max != -inf:
        print(max_index)
    else:
        print('No matches')

def min_even_odd(even_odd):
    min = inf
    min_index = 0
    for i in range(len(list_input)):
        if list_input[i] <= min and list_input[i] % 2 == 0 and even_odd == 'even':
            min = list_input[i]
            min_index = i
        elif list_input[i] <= min and list_input[i] % 2 != 0 and even_odd == 'odd':
            min = list_input[i]
            min_index = i
        else:
            pass

    if min != inf:
        print(min_index)
    else:
        print('No matches')

def first(count, even_odd):
    temp_list = []
    if 0 <= count <= len(list_input):
        for i in range(len(list_input)):
            if list_input[i] % 2 == 0 and even_odd == 'even':
                temp_list.append(list_input[i])
            elif list_input[i] % 2 != 0 and even_odd == 'odd':
                temp_list.append(list_input[i])
            else:
                pass
        print(temp_list[0:count])
    else:
        print(f'Invalid count')

def last(count, even_odd):
    temp_list = []
    if 0 <= count <= len(list_input):
        for i in range(len(list_input)):
            if list_input[i] % 2 == 0 and even_odd == 'even':
                temp_list.append(list_input[i])
            elif list_input[i] % 2 != 0 and even_odd == 'odd':
                temp_list.append(list_input[i])
            else:
                pass
        if count >= len(temp_list):
            print(temp_list)
        else:
            print(temp_list[-count:])
    else:
        print(f'Invalid count')

while end == False:
    command = input()
    split_command = command.split(' ')

    if split_command[0] == 'end':
        end = True
    elif split_command[0] == 'exchange':
        list_input = exchange(int(split_command[1]))
    elif split_command[0] == 'max':
        max_even_odd(split_command[1])
    elif split_command[0] == 'min':
        min_even_odd(split_command[1])
    elif split_command[0] == 'first':
        first(int(split_command[1]), split_command[2])
    elif split_command[0] == 'last':
        last(int(split_command[1]), split_command[2])
    else:
        pass

print(list_input)
