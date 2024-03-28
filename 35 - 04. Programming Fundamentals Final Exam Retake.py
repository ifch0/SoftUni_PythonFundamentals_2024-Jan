# 01. Password Reset

password_string = input()

def take_odd(password_string):
    password_string = password_string[1::2]
    print(password_string)
    return password_string

def cut(password_string, index, length):
    substring = password_string[index:index+length]
    password_string = password_string.replace(substring, "", 1)
    print(password_string)
    return password_string

def substitute(password_string, substring, substitute):
    if substring in password_string:
        password_string = password_string.replace(substring, substitute)
        print(password_string)
    else:
        print(f"Nothing to replace!")
    return password_string

while True:
    user_input = input()

    if user_input == "Done":
        break

    commands = user_input.split()

    if commands[0] == "TakeOdd":
        password_string = take_odd(password_string)
    elif commands[0] == "Cut":
        password_string = cut(password_string, int(commands[1]), int(commands[2]))
    elif commands[0] == "Substitute":
        password_string = substitute(password_string, commands[1], commands[2])
    else:
        pass

print(f"Your password is: {password_string}")

# 02. Fancy Barcodes

import re

qty_inputs = int(input())

for i in range(qty_inputs):
    string_input = input()

    validation_pattern = r"@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+"
    numbers_pattern = r"\d+"

    barcode = re.search(validation_pattern, string_input)

    product_group = ""
    if barcode:
        barcode = barcode.group(1)
        digits = re.findall(numbers_pattern, barcode)
        if len(digits) == 0:
            product_group = "00"
        else:
            for digit in digits:
                product_group += digit
        print(f"Product group: {product_group}")
    else:
        print(f"Invalid barcode")

# 03. Heroes of Code and Logic VII

def cast_spell(heroes, hero_name, mp_needed, spell_name):
    if heroes[hero_name]["mp"] >= mp_needed:
        heroes[hero_name]["mp"] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mp']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")

def take_damage(heroes, hero_name, damage, attacker):
    if heroes[hero_name]["hp"] > damage:
        heroes[hero_name]["hp"] -= damage
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        heroes.pop(hero_name)

def recharge(heroes, hero_name, amount):
    if heroes[hero_name]["mp"] + amount > 200:
        amount = 200 - heroes[hero_name]["mp"]

    heroes[hero_name]["mp"] += amount
    print(f"{hero_name} recharged for {amount} MP!")

def heal(heroes, hero_name, amount):
    if heroes[hero_name]["hp"] + amount > 100:
        amount = 100 - heroes[hero_name]["hp"]

    heroes[hero_name]["hp"] += amount
    print(f"{hero_name} healed for {amount} HP!")

def print_heroes(heroes):
    for hero, stats in heroes.items():
        print(f"{hero}")
        print(f"  HP: {heroes[hero]['hp']}")
        print(f"  MP: {heroes[hero]['mp']}")

qty_inputs = int(input())
heroes = {}
for i in range(qty_inputs):
    name, hp, mp = input().split()

    heroes[name] = {}
    heroes[name]["hp"] = int(hp)
    heroes[name]["mp"] = int(mp)

while True:
    user_input = input()

    if user_input == "End":
        break

    commands = user_input.split(" - ")

    if commands[0] == "CastSpell":
        cast_spell(heroes, commands[1], int(commands[2]), commands[3])
    elif commands[0] == "TakeDamage":
        take_damage(heroes, commands[1], int(commands[2]), commands[3])
    elif commands[0] == "Recharge":
        recharge(heroes, commands[1], int(commands[2]))
    elif commands[0] == "Heal":
        heal(heroes, commands[1], int(commands[2]))
    else:
        pass

print_heroes(heroes)
