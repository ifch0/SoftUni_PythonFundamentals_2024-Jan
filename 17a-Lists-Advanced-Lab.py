# 01. No Vowels

text_input = input()

exclusion_list = ['a', 'e', 'i', 'o', 'u']

filtered_list = ''.join([sym for sym in text_input if sym.lower() not in exclusion_list])

print(filtered_list)

# 02. Trains

qty_wagons = int(input())

wagons = [0] * qty_wagons
end = False

def people_manipulation(wagons, people, command='add', index=-1):
    if command == 'add':
        wagons[index] += people
    elif command == 'remove':
        wagons[index] -= people
    else:
        pass

    return

while end == False:
    user_command = input()

    command_properties = user_command.split(' ')

    if command_properties[0] == 'End':
        end = True
    elif command_properties[0] == 'add':
        people_manipulation(wagons, people=int(command_properties[1]))
    elif command_properties[0] == 'insert':
        people_manipulation(wagons, people=int(command_properties[2]), index=int(command_properties[1]))
    elif command_properties[0] == 'leave':
        people_manipulation(wagons, people=int(command_properties[2]), command='remove', index=int(command_properties[1]))

print(wagons)

# 03. To-do List

index_list = []
task_list = []
sorted_list = []

def fill_task_list(index_list, task_list):
    end = False
    while end == False:
        user_input = input()

        if user_input == 'End':
            end = True
        else:
            index_list.append(int(user_input.split('-')[0]))
            task_list.append(user_input.split('-')[1])

    return

def sort_taks_list(index_list, task_list, sorted_list):
    for i in range(len(index_list)):
        x = index_list.index(min(index_list))
        sorted_list.append(task_list[x])
        index_list.pop(x)
        task_list.pop(x)

    return



fill_task_list(index_list, task_list)
sort_taks_list(index_list, task_list, sorted_list)
print(sorted_list)

# 04. Palindrome Strings

input_list = list(map(str, input().split(' ')))
search_word = input()

palindrome_list = []
found_counter = 0

def find_palindromes(input_list, palindrome_list):
    for word in input_list:
        if word == word[::-1]:
            palindrome_list.append(word)
        else:
            pass

def find_matching_palindrome(palindrome_list, search_string):
    counter = 0
    for i in range(len(palindrome_list)):
        if palindrome_list[i] == search_string:
            counter += 1
        else:
            pass

    return counter

find_palindromes(input_list, palindrome_list)
found_counter = find_matching_palindrome(palindrome_list, search_word)

print(palindrome_list)
print(f'Found palindrome {found_counter} times')

# 05. Sorting Names

input_list = list(map(str, input().split(', ')))

sorted_list = sorted(input_list, key=lambda element: (-len(element), element))

print(sorted_list)

# 06. Even Numbers

input_list = list(map(int, input().split(', ')))

filtered_list = [index for index, num in enumerate(input_list) if num %2 == 0]

print(filtered_list)

# 07. The Office

input_list = list(map(int, input().split(' ')))

average = sum(input_list) / len(input_list)

qty_above_average = len(list(filter(lambda x: x >= average, input_list)))

if qty_above_average >= len(input_list)/2:
    print(f'Score: {qty_above_average}/{len(input_list)}. Employees are happy!')
else:
    print(f'Score: {qty_above_average}/{len(input_list)}. Employees are not happy!')
