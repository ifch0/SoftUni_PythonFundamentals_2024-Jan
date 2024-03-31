# 01. Decrypting Commands

message = input()

def replace(message, current_char, new_char):
    message = message.replace(current_char, new_char)
    print(message)
    return message

def cut(message, start_index, end_index):
    if valid_index(start_index) and valid_index(end_index):
        first_part = message[:start_index]
        last_part = message[end_index+1:]
        new_message = first_part + last_part
        print(new_message)
        return new_message
    else:
        print(f"Invalid indices!")
        return message

def make(message, case):
    if case == "Upper":
        message = message.upper()
    elif case == "Lower":
        message = message.lower()

    print(message)
    return message

def check(message, string):
    if string in message:
        print(f"Message contains {string}")
    else:
        print(f"Message doesn't contain {string}")

def valid_index(index):
    if 0 <= index < len(message):
        return True
    else:
        return False

def sum(message, start_index, end_index):
    temp_string = ""
    total_sum = 0
    if valid_index(start_index) and valid_index(end_index):
        temp_string = message[start_index:end_index+1]
        for char in temp_string:
            total_sum += ord(char)
        print(total_sum)
    else:
        print(f"Invalid indices!")

while True:
    user_input = input()

    if user_input == "Finish":
        break

    commands = user_input.split()

    if commands[0] == "Replace":
        message = replace(message, commands[1], commands[2])
    elif commands[0] == "Cut":
        message = cut(message, int(commands[1]), int(commands[2]))
    elif commands[0] == "Make":
        message = make(message, commands[1])
    elif commands[0] == "Check":
        check(message, commands[1])
    elif commands[0] == "Sum":
        sum(message, int(commands[1]), int(commands[2]))
    else:
        pass

# 02. Message Decrypter

import re

qty_inputs = int(input())
def get_message(string):
    pattern = r"(^(?<!\.)*)([$\%])([A-Z][a-z]{2,})\2\:\s(\[[0-9]+\]\|)(\[[0-9]+\]\|)(\[[0-9]+\]\|)$"
    message = re.findall(pattern, string)
    return message

def get_number(string):
    pattern = r"[0-9]+"
    number = re.findall(pattern, string)
    number = int(number[0])
    return int(number)

for i in range(qty_inputs):
    user_input = input()

    message = get_message(user_input)
    if message:
        chr_1 = chr(get_number(message[0][3]))
        chr_2 = chr(get_number(message[0][4]))
        chr_3 = chr(get_number(message[0][5]))
        print(f"{message[0][2]}: {chr_1}{chr_2}{chr_3}")
    else:
        print("Valid message not found!")

# 03. Dictionary

words_and_definitions = input().split(" | ")
words_for_exam = input().split(" | ")
definitions = {}
command = input()

def split_word(definitions, line):
    word, definition = line.split(": ")

    if word not in definitions:
        definitions[word] = []

    definitions[word].append(definition)

def test(definitions, words):
    for key_word in words:
        for lookup_word, data in definitions.items():
            if key_word == lookup_word:
                print(f"{key_word}:")
                for definition in data:
                    print(f" -{definition}")

def hand_over(definitions):
    output_string = []
    for word in definitions:
        output_string.append(word)

    print(" ".join(output_string))

for each in words_and_definitions:
    split_word(definitions, each)

if command == "Test":
    test(definitions, words_for_exam)
elif command == "Hand Over":
    hand_over(definitions)
