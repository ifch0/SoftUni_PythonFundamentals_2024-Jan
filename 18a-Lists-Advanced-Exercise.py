# 01. Which Are In? (ugly version)

substring_list = list(map(str, input().split(', ')))
string = input()

match_list = []

for i in range(len(substring_list)):
    if substring_list[i] in string:
        match_list.append(substring_list[i])

print(match_list)

# 01. Which Are In? (better version)

substring_list = list(map(str, input().split(', ')))
string_list = list(map(str, input().split(', ')))

match_list = []

for i in range(len(substring_list)):
    for j in range(len(string_list)):
        if substring_list[i] in string_list[j]:
            if substring_list[i] not in match_list:
                match_list.append(substring_list[i])

print(match_list)

# 02. Next Version

version = list(map(int, input().split('.')))

version[2] += 1

if version[2] == 10:
    version[2] = 0
    version[1] += 1

if version[1] == 10:
    version[1] = 0
    version[0] += 1

new_version = '.'.join(map(str, version))

print(new_version)

# 03. Word Filter

word_input = input().split()

filtered_list = [word for word in word_input if len(word) %2 == 0]

for word in filtered_list:
    print(word)

# 04. Number Classification

input_numbers = list(map(int, input().split(', ')))

positive_list = [num for num in input_numbers if num >= 0]
negative_list = [num for num in input_numbers if num < 0]
even_list = [num for num in input_numbers if num % 2 == 0]
odd_list = [num for num in input_numbers if num % 2 != 0]

positive_nums = ', '.join(map(str, positive_list))
negative_nums = ', '.join(map(str, negative_list))
even_nums = ', '.join(map(str, even_list))
odd_nums = ', '.join(map(str, odd_list))

print(f'Positive: {positive_nums}')
print(f'Negative: {negative_nums}')
print(f'Even: {even_nums}')
print(f'Odd: {odd_nums}')

# 05. Office Chairs

qty_meeting_rooms = int(input())

rooms_list = []

need_more_chairs = False

def check_for_chairs(rooms, room):
    global need_more_chairs
    difference = len(rooms[i][0]) - int(rooms_list[i][1])
    rooms[i].append(difference)
    if difference < 0:
        need_more_chairs = True

def print_needed_chairs(rooms):
    for i in range(len(rooms)):
        if rooms[i][2] < 0:
            print(f'{abs(rooms[i][2])} more chairs needed in room {i+1}')

def count_free_space(rooms):
    free_space = 0
    for i in range(len(rooms)):
        free_space += rooms[i][2]

    return free_space

for i in range(qty_meeting_rooms):
    room_equipment = input().split()

    rooms_list.append(room_equipment)

for i in range(qty_meeting_rooms):
    check_for_chairs(rooms_list, i)

if need_more_chairs == True:
    print_needed_chairs(rooms_list)
else:
    free_space = count_free_space(rooms_list)
    print(f'Game On, {free_space} free chairs left')

# 06. Electron Distribution

qty_electrons = int(input())

electron_distribution = []

free_electrons = qty_electrons
layer_counter = 0

def fill_shell(electron_distribution, free_electrons, current_layer):
    needed_electrons = 2 * (current_layer) * (current_layer)
    if needed_electrons <= free_electrons:
        electron_distribution.append(needed_electrons)
        free_electrons -= needed_electrons
    else:
        electron_distribution.append(free_electrons)
        free_electrons -= free_electrons

    return free_electrons

while free_electrons > 0:
    layer_counter += 1
    free_electrons = fill_shell(electron_distribution, free_electrons, layer_counter)

print(electron_distribution)

# 07. Group of 10's

input_numbers = list(map(int, input().split(', ')))

groups = max(input_numbers) // 10 + 1
if max(input_numbers) % 10 == 0:
    groups -= 1
numbers_by_groups = []
for i in range(groups):
    numbers_by_groups.append([])

def sort_number(num, num_groups):
    group_id = num // 10
    if num % 10 == 0:
        group_id -= 1
    num_groups[group_id].append(num)

def print_nums(num_groups):
    for i in range(len(num_groups)):
        print(f'Group of {(i+1) * 10}\'s: {num_groups[i]}')


for i in range(len(input_numbers)):
    sort_number(input_numbers[i], numbers_by_groups)

print_nums(numbers_by_groups)

# 08. Decipher This!

input_text = list(map(str, input().split(' ')))

def digist_to_letter(word):
    char_list = list(word)
    num_list = []

    while True:
        if char_list[0].isdigit():
            num_list.append(char_list[0])
            char_list.pop(0)
        else:
            break

    num_list = ''.join(num_list)
    missing_letter = list(chr(int(num_list)))
    char_list = missing_letter + char_list

    return ''.join(char_list)

def swap_letters(word):
    char_list = list(word)
    char_list[1], char_list[-1] = char_list[-1], char_list[1]
    return ''.join(char_list)

for i in range(len(input_text)):
    input_text[i] = digist_to_letter(input_text[i])
    input_text[i] = swap_letters(input_text[i])

output_string = ' '.join(input_text)
print(output_string)

# 09. Anonymous Threat (70/100)

input_text = list(map(str, input().split(' ')))

def command_merge(work_list, start_index, end_index):
    if start_index < 0:
        start_index = 0
    if start_index > len(work_list) - 1:
            start_index = len(work_list) - 1
    if end_index < 0:
        end_index = 0
    if end_index > len(work_list) - 1:
            end_index = len(work_list) - 1

    leading_list = []

    if start_index == 0:
        pass
    else:
        for i in range(start_index):
            leading_list.append(work_list[i])

    trailing_list = []

    if end_index == len(work_list) - 1:
        pass
    else:
        for i in range(len(work_list) - end_index - 1):
            trailing_list.append(work_list[end_index + i + 1])

    temp_list = []

    for i in range(end_index - start_index + 1):
        temp_list.append(work_list[start_index + i])


    mid_string = ''.join(temp_list)
    leading_list.append(mid_string)
    output_list = leading_list + trailing_list

    return output_list

def command_divide(work_list, element_index, partitions):
    char_list = list(work_list[element_index])
    new_strings_length = len(char_list) // partitions

    temp_list = []

    for i in range(partitions - 1):
        temp_string = ''
        for j in range(new_strings_length):
            temp_string += char_list.pop(0)
        temp_list.append(temp_string)

    temp_string = ''
    for i in range(len(char_list)):
        temp_string += char_list.pop(0)
    temp_list.append(temp_string)

    leading_list = []

    if element_index == 0:
        pass
    else:
        for i in range(element_index):
            leading_list.append(work_list[i])

    trailing_list = []

    if element_index == len(work_list) - 1:
        pass
    else:
        for i in range(len(work_list) - element_index):
            trailing_list.append(work_list[element_index + i])

    output_list = leading_list + temp_list + trailing_list
    return output_list

end = False
while end == False:
    command = list(map(str, input().split(' ')))

    if command[0] == '3:1':
        end = True
    elif command[0] == 'merge':
        input_text = command_merge(input_text, int(command[1]), int(command[2]))
    elif command[0] == 'divide':
        input_text = command_divide(input_text, int(command[1]), int(command[2]))
    else:
        pass

output_string = ' '.join(input_text)
print(output_string)

# 10. Pokemon Don't Go

pokemon_list = list(map(int, input().split(' ')))

end = False

total_moves = 0

def recalculate_distance(pokemon_list, new_distance):
    for i in range(len(pokemon_list)):
        if pokemon_list[i] <= new_distance:
            pokemon_list[i] += new_distance
        else:
            pokemon_list[i] -= new_distance

def remove_and_recalculate(pokemon_list, index, total_moves):
    new_distance = pokemon_list[index]

    pokemon_list.pop(index)

    recalculate_distance(pokemon_list, new_distance)

    total_moves += new_distance
    return pokemon_list, total_moves

def replace_first(pokemon_list, index, total_moves):
    new_distance = pokemon_list[0]

    pokemon_list[0] = pokemon_list[-1]

    recalculate_distance(pokemon_list, new_distance)

    total_moves += new_distance
    return pokemon_list, total_moves

def replace_last(pokemon_list, index, total_moves):
    new_distance = pokemon_list[-1]

    pokemon_list[-1] = pokemon_list[0]

    recalculate_distance(pokemon_list, new_distance)

    total_moves += new_distance
    return pokemon_list, total_moves

while end == False:
    index_to_remove = int(input())

    if index_to_remove < 0:
        pokemon_list, total_moves = replace_first(pokemon_list, index_to_remove, total_moves)
    elif index_to_remove >= len(pokemon_list):
        pokemon_list, total_moves = replace_last(pokemon_list, index_to_remove, total_moves)
    else:
        pokemon_list, total_moves = remove_and_recalculate(pokemon_list, index_to_remove, total_moves)

    if len(pokemon_list) == 0:
        end = True

print(total_moves)

# 11. SoftUni Course Planning (88/100)

courses_list = list(map(str, input().split(', ')))

end = False

def add_course(schedule, title):
    if title not in schedule:
        schedule.append(title)

def insert_course(schedule, title, position):
    if title not in schedule:
        schedule.insert(position, title)

def remove_course(schedule, title):
    if title in schedule:
        schedule.remove(title)

def swap_courses(schedule, title_1, title_2):
    if title_1 in schedule and title_2 in schedule:
        index_1 = schedule.index(title_1)
        index_2 = schedule.index(title_2)
        schedule[index_1], schedule[index_2] = schedule[index_2], schedule[index_1]

        # Now (if both courses exists and we swapped them) we have a list with courses like this:
        # [a] [b] [title_2] [c] [d] [title_1] [e] [f]
        # and have to check if [c] and [e] are exercises and move them if needed

        if index_2 + 1 < len(schedule):
            exercise_1_check = schedule[index_2 + 1].split('-')
            if exercise_1_check[0] == schedule[index_1]:
                schedule.insert(index_1 + 1, schedule.pop(index_2 + 1))
        if index_1 + 1 < len(schedule):
            exercise_2_check = schedule[index_1 + 1].split('-')
            if exercise_2_check[0] == schedule[index_2]:
                schedule.insert(index_2 + 1, schedule.pop(index_1 + 1))

def add_exercise(schedule, title):
    if title in schedule:
        index_course = schedule.index(title)
        if index_course + 1 < len(schedule):
            exercise_check = schedule[index_course + 1].split('-')
            if exercise_check[0] == schedule[index_course]:
                pass
            else:
                schedule.insert(index_course + 1, title + '-Exercise')
        else:
            schedule.append(title + '-Exercise')
    else:
        schedule.append(title)
        schedule.append(title + '-Exercise')

def print_schedule(schedule):
    for i in range(len(schedule)):
        print(f'{i+1}.{schedule[i]}')

while end == False:
    command_input = list(map(str, input().split(':')))

    if command_input[0] == 'course start':
        end = True
    elif command_input[0] == 'Add':
        add_course(courses_list, command_input[1])
    elif command_input[0] == 'Insert':
        insert_course(courses_list, command_input[1], int(command_input[2]))
    elif command_input[0] == 'Remove':
        remove_course(courses_list, command_input[1])
    elif command_input[0] == 'Swap':
        swap_courses(courses_list, command_input[1], command_input[2])
    elif command_input[0] == 'Exercise':
        add_exercise(courses_list, command_input[1])
    else:
        pass

print_schedule(courses_list)
