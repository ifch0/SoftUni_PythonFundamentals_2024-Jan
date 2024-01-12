# 01. Jenny's Secret Message

username = input()

if username == 'Johnny':
    print(f'Hello, my love!')
else:
    print(f'Hello, {username}!')

# 02. Drink Something

user_age = int(input())

drink = ''

if user_age <= 14:
    drink = 'toddy'
elif user_age <= 18:
    drink = 'coke'
elif user_age <= 21:
    drink = 'beer'
else:
    drink = 'whisky'

print(f'drink {drink}')

# 03. Chat Codes

qty_inputs = int(input())

for i in range(qty_inputs):
    user_input = int(input())

    if user_input == 88:
        print(f'Hello')
    elif user_input == 86:
        print(f'How are you?')
    elif user_input < 88:
        print(f'GREAT!')
    elif user_input > 88:
        print(f'Bye.')
    else:
        pass

# 04. Maximum Multiple

divisor = int(input())
boundary = int(input())

found = False
current_number = boundary

while found == False:
    if current_number % divisor == 0:
        print(current_number)
        found = True
    else:
        current_number -= 1

# 05. Orders

qty_orders = int(input())

prc_capsule = 0
min_prc_capsule = 0.01
max_prc_capsule = 100
qty_days = 0
min_qty_days = 1
max_qty_days = 31
capsules_per_day = 0
min_caps_per_day = 1
max_caps_per_day = 2000

order_total = 0
grand_total = 0

for order in range(qty_orders):
    prc_capsule = float(input())
    qty_days = int(input())
    capsules_per_day = int(input())

    if min_prc_capsule <= prc_capsule <= max_prc_capsule and min_qty_days <= qty_days <= max_qty_days and min_caps_per_day <= capsules_per_day <= max_caps_per_day:
        order_total = prc_capsule * qty_days * capsules_per_day
        grand_total += order_total
        print(f'The price for the coffee is: ${order_total:.2f}')
    else:
        pass

print(f'Total: ${grand_total:.2f}')

# 06. String Pureness

qty_strings = int(input())

for i in range(qty_strings):
    current_string = input()

    if current_string.find(",") == -1 and current_string.find(".") == -1 and current_string.find("_") == -1:
        print(f'{current_string} is pure.')
    else:
        print(f'{current_string} is not pure!')

# 07. Double Char

while True:
    input_string = input()

    if input_string == "End":
        break
    elif input_string == "SoftUni":
        pass
    else:
        for char in input_string:
            print(2 * char, end='')
        print()

# 08. How Much Coffee Do You Need?

end = False

total_coffees = 0

while end == False:
    user_input = input()

    if user_input == 'END':
        end = True
    elif user_input == 'coding' or user_input == 'dog' or user_input == 'cat' or user_input == 'movie':
        total_coffees += 1
    elif user_input == 'CODING' or user_input == 'DOG' or user_input == 'CAT' or user_input == 'MOVIE':
        total_coffees += 2
    else:
        pass

if total_coffees > 5:
    print(f'You need extra sleep')
else:
    print(f'{total_coffees}')

# 09. Sorting Hat

end = False

while end == False:
    user_name = input()

    if user_name == 'Welcome!':
        print(f'Welcome to Hogwarts.')
        end = True
    elif user_name == 'Voldemort':
        print(f'You must not speak of that name!')
        end = True
    elif len(user_name) < 5:
        print(f'{user_name} goes to Gryffindor.')
    elif len(user_name) == 5:
        print(f'{user_name} goes to Slytherin.')
    elif len(user_name) == 6:
        print(f'{user_name} goes to Ravenclaw.')
    else:
        print(f'{user_name} goes to Hufflepuff.')

# 10. Mutate Strings

string_1 = input()
string_2 = input()

for i in range(len(string_1)):
    if string_1[i] == string_2[i]:
        pass
    else:
        temp = list(string_1)
        temp[i] = string_2[i]
        string_1 = "".join(temp)
        print(string_1)

# 11. Easter Bread

budget = float(input())
prc_flour = float(input())

prc_eggs = prc_flour * 0.75
liter_milk = prc_flour * 1.25
prc_milk = liter_milk / 4

loaf_price = prc_eggs + prc_flour + prc_milk
total_loaves = 0
colored_eggs = 0

while budget >= loaf_price:
    budget -= loaf_price
    total_loaves += 1
    colored_eggs += 3

    if total_loaves % 3 == 0:
        colored_eggs -= total_loaves - 2

print(f'You made {total_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

# 12. Christmas Spirit

qty_items = int(input())
days_until_christmas = int(input())

total_spent = 0
total_points = 0

prc_ornament_set = 2
pts_ornament_set = 5
prc_tree_skirt = 5
pts_tree_skirt = 3
prc_tree_garland = 3
pts_tree_garland = 10
prc_tree_lights = 15
pts_tree_lights = 17

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        qty_items += 2

    if day % 2 == 0:
        total_spent += qty_items * prc_ornament_set
        total_points += pts_ornament_set

    if day % 3 == 0:
        total_spent += qty_items * (prc_tree_skirt + prc_tree_garland)
        total_points += (pts_tree_skirt + pts_tree_garland)

    if day % 5 == 0:
        total_spent += qty_items * prc_tree_lights
        total_points += pts_tree_lights
        if day % 3 == 0:
            total_points += 30

    if day % 10 == 0:
        total_points -= 20
        total_spent += prc_tree_skirt + prc_tree_garland + prc_tree_lights

if days_until_christmas % 10 == 0:
    total_points -= 30

print(f'Total cost: {total_spent}')
print(f'Total spirit: {total_points}')
