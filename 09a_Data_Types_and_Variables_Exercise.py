# 01. Integer Operations

first_num = int(input())
second_num = int(input())
third_num = int(input())
fourth_num = int(input())

result = (first_num + second_num) // third_num * fourth_num

print(f'{result}')

# 02. Chars to String

first_char = input()
second_char = input()
third_char = input()

result = first_char + second_char + third_char

print(f'{result}')

# 03. Elevator

total_people = int(input())
capacity = int(input())

courses = 0

while total_people > 0:
    total_people -= capacity
    courses += 1

print(f'{courses}')

# 04. Sum of Chars

num_of_chars = int(input())

total_sum = 0

for i in range(num_of_chars):
    char_input = input()
    total_sum += ord(char_input)

print(f'The sum equals: {total_sum}')

# 05. Print Part of the ASCII Table

start_index = int(input())
end_index = int(input())

for i in range(start_index, end_index + 1):
    print(f'{chr(i)}', end='')
    if i != end_index:
        print(f' ', end='')

# 06. Triples of Latin Letters

num_of_chars = int(input())

for char_1 in range(97, 97 + num_of_chars):
    for char_2 in range(97, 97 + num_of_chars):
        for char_3 in range(97, 97 + num_of_chars):
            print(f'{chr(char_1)}{chr(char_2)}{chr(char_3)}')

# 07. Water Overflow

qty_inputs = int(input())

tank_capacity = 255
tank_current_capacity = 0

for i in range(qty_inputs):
    current_input = int(input())
    if tank_current_capacity + current_input > tank_capacity:
        print(f'Insufficient capacity!')
    else:
        tank_current_capacity += current_input

print(f'{tank_current_capacity}')

# 08. Party Profit

group_size = int(input())
qty_days = int(input())

current_money = 0

for day in range(1, qty_days + 1):
    current_money += 50
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5

    current_money -= group_size * 2

    if day % 3 == 0:
        current_money -= group_size * 3
    if day % 5 == 0:
        current_money += group_size * 20
        if day % 3 == 0:
            current_money -= group_size * 2

money_per_person = current_money / group_size

print(f'{group_size} companions received {int(money_per_person)} coins each.')

# 09. Snowballs

qty_snowballs = int(input())

best_weight_snowball = 0
best_time_flight = 0
best_quality_snowball = 0

best_snowball = 0

for snowball in range(qty_snowballs):
    current_weight_snowball = int(input())
    current_time_flight = int(input())
    current_quality_snowball = int(input())

    current_best_snowball = (current_weight_snowball / current_time_flight) ** current_quality_snowball

    if current_best_snowball > best_snowball:
        best_snowball = current_best_snowball
        best_weight_snowball = current_weight_snowball
        best_time_flight = current_time_flight
        best_quality_snowball = current_quality_snowball

print(f'{best_weight_snowball} : {best_time_flight} = {int(best_snowball)} ({best_quality_snowball})')

# 10. Gladiator Expenses

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

current_expenses = 0

for fight in range(1, lost_fights +1):
    if fight % 2 == 0:
        current_expenses += helmet_price
    if fight % 3 == 0:
        current_expenses += sword_price
    if fight % 6 == 0:
        current_expenses += shield_price
    if fight % 12 == 0:
        current_expenses += armor_price

print(f'Gladiator expenses: {current_expenses:.2f} aureus')
