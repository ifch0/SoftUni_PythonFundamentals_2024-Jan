# 01. Burger Bus

qty_cities = int(input())

total_earned = 0

event_ratio = 1.5
rain_ratio = 0.9

for city in range(1, qty_cities + 1):
    current_profit = 0
    city_name = input()
    money_earned = float(input())
    expenses = float(input())

    if ( city % 3 == 0 and city % 5 == 0) or city % 5 == 0:
        money_earned *= rain_ratio
    elif city %3 == 0:
        expenses *= event_ratio

    current_profit = money_earned - expenses
    total_earned += current_profit

    print(f'In {city_name} Burger Bus earned {current_profit:.2f} leva.')

print(f'Burger Bus total profit: {total_earned:.2f} leva.')

# 02. Coffee Lover

coffee_list = input().split()
qty_commands = int(input())

def include(coffee):
    coffee_list.append(coffee)

def remove(which, quantity):
    order = 0
    if quantity <= len(coffee_list):
        if which == 'last':
            order = -1
        for i in range(quantity):
            coffee_list.pop(order)

def prefer(index_1, index_2):
    if index_1 >= 0 and index_2 >= 0 and index_1 <= len(coffee_list) - 1 and index_2 <= len(coffee_list) - 1:
        coffee_list[index_1], coffee_list[index_2] = coffee_list[index_2], coffee_list[index_1]

def reverse_list():
    coffee_list.reverse()

def print_list():
    print(f'Coffees:')
    print(*coffee_list)

for i in range(qty_commands):
    command = input().split()

    if command[0] == 'Include':
        include(command[1])
    elif command[0] == 'Remove':
        remove(command[1], int(command[2]))
    elif command[0] == 'Prefer':
        prefer(int(command[1]), int(command[2]))
    elif command[0] == 'Reverse':
        reverse_list()
    else:
        pass

print_list()

# 03. School Library

books_list = input().split('&')

on_the_shelf = lambda x: x in books_list
find_book = lambda x: books_list.index(x)

def add_book(book_name):
    if not on_the_shelf(book_name):
        books_list.insert(0, book_name)

def take_book(book_name):
    if on_the_shelf(book_name):
        books_list.pop(find_book(book_name))

def swap_books(book_1, book_2):
    if on_the_shelf(book_1) and on_the_shelf(book_2):
        books_list[find_book(book_2)], books_list[find_book(book_1)] = books_list[find_book(book_1)], books_list[find_book(book_2)]

def check_book(index):
    if abs(index) <= len(books_list):
        print(books_list[index])

def insert_book(book_name):
    if not on_the_shelf(book_name):
        books_list.append(book_name)

done = False
while done == False:
    input_command = input().split(' | ')

    if input_command[0] == 'Done':
        done = True
    elif input_command[0] == 'Add Book':
        add_book(input_command[1])
    elif input_command[0] == 'Take Book':
        take_book(input_command[1])
    elif input_command[0] == 'Swap Books':
        swap_books(input_command[1], input_command[2])
    elif input_command[0] == 'Insert Book':
        insert_book(input_command[1])
    elif input_command[0] == 'Check Book':
        check_book(int(input_command[1]))
    else:
        pass

print(', '.join(books_list))
