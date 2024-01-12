# 01. Find The Largest

input_string = input()

input_list = list(map(int, input_string))
output_list = []

for i in range(len(input_list)):
    temp_max_value = -1
    temp_index = 0

    for x in range(len(input_list)):
        if input_list[x] > temp_max_value:
            temp_max_value = input_list[x]
            temp_index = x

    input_list[temp_index] = 0
    output_list .append(str(temp_max_value))

output_string = "".join(output_list)
print(f'{output_string}')

# 02. Find The Capitals

input_string = input()

output_list = []

for i in range(len(input_string)):
    if 65 <= ord(input_string[i]) <= 90:
        output_list .append(i)

print(f'{output_list}')

# 03. Wolf In Sheep's Clothing

input_string = input()

input_list = input_string.split(", ")

for i in range(len(input_list)):
    if input_list[i] == "wolf":
        if i != len(input_list) - 1:
            print(f'Oi! Sheep number {(len(input_list) - 1) - i}! You are about to be eaten by a wolf!')
        else:
            print(f'Please go away and stop eating my sheep')

# 04. Sum Of A Beach

input_string = input()

search_items = ["sand", "water", "fish", "sun"]

counter = 0

lowercase_string = str.lower(input_string)

for i in range(len(search_items)):
    start_index = 0
    for x in range(len(lowercase_string)):
        y = lowercase_string.find(search_items[i], start_index)
        if y != -1:
            start_index = y+1
            counter += 1

print(f'{counter}')
