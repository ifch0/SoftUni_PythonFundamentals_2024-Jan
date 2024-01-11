# 01. Number Definer

number = float(input())

if number == 0:
    print('zero')
elif abs(number) < 1:
    print('small ', end='')
elif abs(number) > 1000000:
    print('large ', end='')
else:
    pass

if number < 0:
    print('negative')
elif number > 0:
    print('positive')
else:
    pass

# 02. Largest Of Three Numbers

from math import inf

inputs = 3

max_num = -inf

for i in range(inputs):
    number = int(input())

    if number > max_num:
        max_num = number

print(f'{max_num}')

# 03. Word Reverse

word = input()

for i in range(len(word) - 1, -1, -1):
    print(f'{word[i]}', end='')

# 04. Even Numbers

total_inputs = int(input())

for i in range(total_inputs):
    number_input = int(input())

    if number_input % 2 != 0:
        print(f'{number_input} is odd!')
        break
else:
    print(f'All numbers are even.')

# 05. Number Between 1 and 100

while True:
    input_number = float(input())

    if 1 <= input_number <= 100:
        print(f'The number {input_number} is between 1 and 100')
        break

# 06. Shopping

budget = int(input())

total_spent = 0

while True:
    user_input = input()

    if user_input == 'End':
        print(f'You bought everything needed.')
        break
    else:
        total_spent += int(user_input)
        if total_spent > budget:
            print(f'You went in overdraft!')
            break

# 07. Patterns

stars = int(input())

for i in range(1, stars):
    print(i * '*')

for i in range(stars, 0, -1):
    print(i * '*')
