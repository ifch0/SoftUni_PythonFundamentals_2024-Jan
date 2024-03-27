# 01. Race

import re

racers = input().split(", ")
racers_and_points = {}

find_letters = r"[a-zA-Z]"
find_digits = r"\d"

while True:
    user_input = input()

    if user_input == "end of race":
        break
    else:
        letters = re.findall(find_letters, user_input)
        digits = re.findall(find_digits, user_input)
        name = "".join(letters)
        if name in racers:
            if name not in racers_and_points:
                racers_and_points[name] = 0
            points = 0
            for digit in digits:
                points += int(digit)
            racers_and_points[name] += points

racers_and_points = dict(sorted(racers_and_points.items(), key=lambda x: -x[1]))

racers = []
for racer, distance in racers_and_points.items():
    racers.append(racer)

print(f"1st place: {racers[0]}")
print(f"2nd place: {racers[1]}")
print(f"3rd place: {racers[2]}")

# 02. SoftUni Bar Income

import re

pattern = r"%([A-Z][a-z]*)%(.*)\<(\w+)\>(.*)\|([0-9]+)\|([a-zA-Z]*)([0-9]+(\.[0-9]+)*)\$"

total_income = 0
while True:
    user_input = input()

    if user_input == "end of shift":
        break
    else:
        split_input = re.findall(pattern, user_input)
        if split_input:
            name = split_input[0][0]
            product = split_input[0][2]
            qty = int(split_input[0][4])
            single_price = float(split_input[0][6])
            total_price = qty * single_price
            total_income += total_price

            print(f"{name}: {product} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")

# 03. Star Enigma

import re

key_letters = "star"

def calculate_key(message):
    counter = 0
    for letter in key_letters:
        counter += message.lower().count(letter)
    return counter

def decrypt_message(message, decr_key):
    new_message = ""
    for symbol in message:
        new_symbol = chr(ord(symbol) - decr_key)
        new_message += new_symbol
    return new_message

def validate_message(message_parts):
    if message_parts:
        print(message_parts.groups())
        if message_parts.group(1).isalpha() and message_parts.group(5).isnumeric() and message_parts.group(11).isnumeric():
            return True
    return False

planets = {"Attacked planets": [], "Destroyed planets": []}
def process_message(message):
    #search_pattern = r"(\@([a-zA-Z]+))(.*)(\:(\d+))(.*)(\!([A|D])\!)(.*)(\-\>(\d+))(.*)"
    #search_pattern = r"(\@([a-zA-Z]+))(\w*)(\:(\d+))(\w*)(\!([A|D])\!)(\w*)(\-\>(\d+))(\w*)"
    search_pattern = r"(\@([a-zA-Z]+))([^\@\-\!\:\>]*)(\:(\d+))([^\@\-\!\:\>]*)(\!([A|D])\!)([^\@\-\!\:\>]*)(\-\>(\d+))([^\@\-\!\:\>]*)"
    message_parts = re.search(search_pattern, message)
    #validate_message(message_parts)
    if message_parts:
        planet_name = message_parts.group(2)
        attack_type = message_parts.group(8)
        if attack_type == "A":
            planets["Attacked planets"].append(planet_name)
        elif attack_type == "D":
            planets["Destroyed planets"].append(planet_name)

def print_planets():
    for type_of_damage, planets_names in planets.items():
        print(f"{type_of_damage}: {len(planets_names)}")
        for planet_name in sorted(planets_names):
            print(f"-> {planet_name}")

qty_messages = int(input())
for i in range(qty_messages):
    encrypted_message = input()

    decr_key = calculate_key(encrypted_message)
    decrypted_message = decrypt_message(encrypted_message, decr_key)
    process_message(decrypted_message)

print_planets()

# 04. Nether Realms

import re

def calculate_health(name):
    health = 0
    symbols_pattern = r"([^0-9\+\-\*\/\.])"
    valid_symbols = "".join(re.findall(symbols_pattern, name))
    for sym in valid_symbols:
        health += int(ord(sym))
    demons_specs[name]["health"] = health

def calculate_damage(name):
    digits_pattern = r"([\+\-]*\d+\.*\d*)"
    valid_digits = list(float(x) for x in (re.findall(digits_pattern, name)))
    damage = sum(valid_digits)

    for ch in name:
        if ch == "*":
            damage *= 2
        elif ch == "/":
            damage /= 2

    demons_specs[name]["damage"] = damage

user_input = input()
demons_specs = {}
split_pattern = r"(,\s*)"
demons = re.sub(split_pattern, " ", user_input).split()

for demon in demons:
    demons_specs[demon] = {}
    calculate_health(demon)
    calculate_damage(demon)

demons_specs = dict(sorted(demons_specs.items(), key=lambda x: x[0]))

for demon_name, specs in demons_specs.items():
    print(f"{demon_name} - {specs['health']} health, {specs['damage']:.2f} damage")


# 05. HTML Parser

import re

def clean_new_line(string):
    clean_string = re.sub(new_line_pattern, "", string)
    return clean_string

def strip_html_tags(string):
    clean_string = re.sub(html_tags_pattern, "", string)
    return clean_string

user_input = input()

title_pattern = r"<title>(.*)<\/title>"
body_pattern = r"<body>(.*)<\/body>"
new_line_pattern = r"\\n"
html_tags_pattern = r"<[^<>]*>"

title = re.findall(title_pattern, user_input)
body_pattern = re.findall(body_pattern, user_input)

clean_title = strip_html_tags(clean_new_line(title[0]))
clean_content = strip_html_tags(clean_new_line(body_pattern[0]))

print(f"Title: {clean_title}")
print(f"Content: {clean_content}")
