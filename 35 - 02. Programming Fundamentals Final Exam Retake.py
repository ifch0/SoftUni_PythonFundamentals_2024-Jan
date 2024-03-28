# 01. World Tour

travel_string = input()

def is_valid(index):
    if index >= 0 and index < len(travel_string):
        return True
    return False

def add_stop(work_string, index, new_string):
    if is_valid(index):
        work_string = work_string[0:index] + new_string + work_string[index:]
    return work_string

def remove_stop(work_string, start_index, end_index):
    if is_valid(start_index) and is_valid(end_index):
        start_string = work_string[0:start_index]
        end_string = work_string[end_index+1:]
        work_string = start_string + end_string
    return work_string

def switch(work_string, old_string, new_string):
    if old_string in work_string:
        work_string = work_string.replace(old_string, new_string)
    return work_string

while True:
    input_command = input()

    if input_command == "Travel":
        break

    commands = input_command.split(":")

    if commands[0] == "Add Stop":
        travel_string = add_stop(travel_string, int(commands[1]), commands[2])
    elif commands[0] == "Remove Stop":
        travel_string = remove_stop(travel_string, int(commands[1]), int(commands[2]))
    elif commands[0] == "Switch":
        travel_string = switch(travel_string, commands[1], commands[2])
    else:
        pass
    print(travel_string)

print(f"Ready for world tour! Planned stops: {travel_string}")

# 02. Destination Mapper

import re

user_input = input()

pattern = r"(\=|\/)([A-Z][a-zA-Z][a-zA-Z]+)\1"

destinations = re.findall(pattern, user_input)
valid_destinations = []
travel_points = 0

for desination in destinations:
    valid_destinations.append(desination[1])
    travel_points += len(desination[1])

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")

# 03. Plant Discovery

plants = {}

def is_valid(plant):
    if plant in plants:
        return True
    print(f"error")
    return False

def rate(plant, rating):
    plants[plant]["rating"].append(rating)

def update(plant, new_rarity):
    plants[plant]["rarity"] = new_rarity

def reset(plant):
    plants[plant]["rating"] = []

def calc_average(ratings):
    if len(ratings) > 0:
        average = sum(ratings) / len(ratings)
        return average
    return 0

qty_inputs = int(input())
for i in range(qty_inputs):
    plant, rarity = input().split("<->")

    if plant not in plants:
        plants[plant] = {"rarity": 0, "rating": []}

    plants[plant]["rarity"] = int(rarity)

while True:
    user_input = input()

    if user_input == "Exhibition":
        break

    commands = user_input.split(" ")

    if is_valid(commands[1]):
        if commands[0] == "Rate:":
            rate(commands[1], float(commands[3]))
        elif commands[0] == "Update:":
            update(commands[1], int(commands[3]))
        elif commands[0] == "Reset:":
            reset(commands[1])

print(f"Plants for the exhibition:")

for plant, specs in plants.items():
    average = calc_average(specs["rating"])
    print(f"- {plant}; Rarity: {specs['rarity']}; Rating: {average:.2f}")
