# 01. The Imitation Game

encrypted_message = input()

def move(message, number_of_letters):
    substring = message[0:number_of_letters]
    message = message[number_of_letters:] + substring
    return message

def insert(message, index, value):
    message = message[0:index] + value + message[index:]
    return message

def change_all(message, substring, replacement):
    message = message.replace(substring, replacement)
    return message
    pass

while True:
    input_command = input()

    if input_command == "Decode":
        break

    commands = input_command.split("|")

    if commands[0] == "Move":
        encrypted_message = move(encrypted_message, int(commands[1]))
    elif commands[0] == "Insert":
        encrypted_message = insert(encrypted_message, int(commands[1]), commands[2])
    elif commands[0] == "ChangeAll":
        encrypted_message = change_all(encrypted_message, commands[1], commands[2])
    else:
        pass

print(f"The decrypted message is: {encrypted_message}")

# 02. Ad Astra

import re

pattern = r"(\#|\|)([a-zA-Z\s]+)\1(\d\d\/\d\d\/\d\d)\1(\d+)\1"

user_input = input()

inventory = re.findall(pattern, user_input)

calories_needed = 2000
total_calories = 0

for group in inventory:
    total_calories += int(group[3])

possible_days = total_calories // calories_needed

print(f"You have food to last you for: {possible_days} days!")

for group in inventory:
    print(f"Item: {group[1]}, Best before: {group[2]}, Nutrition: {group[3]}")

# 03. The Pianist

def add(piece, composer, key, new=False):
    if piece in piano_pieces:
        print(f"{piece} is already in the collection!")
    else:
        piano_pieces[piece] = {}
        piano_pieces[piece]["composer"] = composer
        piano_pieces[piece]["key"] = key
        if new:
            print(f"{piece} by {composer} in {key} added to the collection!")

def remove(piece):
    if piece in piano_pieces:
        piano_pieces.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

def change_key(piece, new_key):
    if piece in piano_pieces:
        piano_pieces[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

initial_inputs = int(input())
piano_pieces = {}
for i in range(initial_inputs):
    piece, composer, key = input().split("|")
    add(piece, composer, key)

while True:
    user_input = input()
    if user_input == "Stop":
        break

    commands = user_input.split("|")

    if commands[0] == "Add":
        add(commands[1], commands[2], commands[3], True)
    elif commands[0] == "Remove":
        remove(commands[1])
    elif commands[0] == "ChangeKey":
        change_key(commands[1], commands[2])
    else:
        pass

for piece, piece_data in piano_pieces.items():
    composer = piece_data["composer"]
    key = piece_data["key"]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
