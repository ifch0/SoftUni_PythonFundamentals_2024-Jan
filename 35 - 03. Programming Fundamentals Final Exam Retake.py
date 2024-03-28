# 01. Secret Chat

message = input()

def insert_space(message, index):
    msg_start = message[0:index]
    msg_end = message[index:]
    message = msg_start + " " + msg_end
    print(message)
    return message

def reverse(message, substring):
    if substring in message:
        replacement = substring[::-1]
        message = message.replace(substring, "", 1)
        message += replacement
        print(message)
    else:
        print(f"error")
    return message

def change_all(message, substring, replacement):
    message = message.replace(substring, replacement)
    print(message)
    return message

while True:
    user_input = input()

    if user_input == "Reveal":
        break

    commands = user_input.split(":|:")

    if commands[0] == "InsertSpace":
        message = insert_space(message, int(commands[1]))
    elif commands[0] == "Reverse":
        message = reverse(message, commands[1])
    elif commands[0] == "ChangeAll":
        message = change_all(message, commands[1], commands[2])
    else:
        pass

print(f"You have a new text message: {message}")

# 02. Mirror Words

import re

user_input = input()

#pairs_pattern = r"((\@|\#)([a-zA-Z]{3,}+)\2\2([a-zA-Z]{3,})\2)"
pairs_pattern = r"((\@|\#)([a-zA-Z][a-zA-Z][a-zA-Z]+)\2\2([a-zA-Z][a-zA-Z][a-zA-Z]+)\2)"

pairs = re.findall(pairs_pattern, user_input)
mirrors = []

for pair in pairs:
    if pair[2] == pair[3][::-1]:
        mirrors.append(f"{pair[2]} <=> {pair[3]}")

if len(pairs) == 0:
    print(f"No word pairs found!")
else:
    print(f"{len(pairs)} word pairs found!")

if len(mirrors) == 0:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    print(", ".join(mirrors))

# 03. Need for Speed III

def drive(cars, car, distance, fuel):
    if cars[car]["fuel"] >= fuel:
        cars[car]["fuel"] -= fuel
        cars[car]["mileage"] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)
    else:
        print(f"Not enough fuel to make that ride")

def refuel(cars, car, fuel):
    tank_capacity = 75
    if cars[car]["fuel"] + fuel > tank_capacity:
        fuel = tank_capacity - cars[car]["fuel"]
    cars[car]["fuel"] += fuel
    print(f"{car} refueled with {fuel} liters")

def revert(cars, car, kilometers):
    if cars[car]["mileage"] - kilometers < 10000:
        cars[car]["mileage"] = 10000
    else:
        cars[car]["mileage"] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")

qty_inputs = int(input())
my_cars = {}
for i in range(qty_inputs):
    car, mileage, fuel = input().split("|")

    my_cars[car] = {}
    my_cars[car]["mileage"] = int(mileage)
    my_cars[car]["fuel"] = int(fuel)

while True:
    user_input = input()
    if user_input == "Stop":
        break

    commands = user_input.split(" : ")

    if commands[0] == "Drive":
        drive(my_cars, commands[1], int(commands[2]), int(commands[3]))
    elif commands[0] == "Refuel":
        refuel(my_cars, commands[1], int(commands[2]))
    elif commands[0] == "Revert":
        revert(my_cars, commands[1], int(commands[2]))
    else:
        pass

for car, stats in my_cars.items():
    print(f"{car} -> Mileage: {stats['mileage']} kms, Fuel in the tank: {stats['fuel']} lt.")
