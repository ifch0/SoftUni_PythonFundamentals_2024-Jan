# 01. Ranking

contests_and_passwords = {}     # {"contest1": "password1", "contest2": "password2"}
users_and_contests = {}         # {"user1": {"contest1": "points", "contest2": "points"}, "user2": {"contest1": "points"}}
users_and_total_points = {}           # {"User1": total_points, "user2": total_points}
user_max_points = 0
user_with_max_points = ""

def valid_contest(contest):
    if contest in contests_and_passwords.keys():
        return True
    return False

def valid_password(contest, password):
    if contests_and_passwords[contest] == password:
        return True
    return False

def create_username_if_does_not_exist(username):
    if username not in users_and_contests.keys():
        users_and_contests[username] = {}

def add_points_if_higher(contest, username, points):
    user_data = users_and_contests[username]
    if contest not in user_data.keys():
        users_and_contests[username][contest] = 0
    if users_and_contests[username][contest] < points:
        users_and_contests[username][contest] = points

end_of_contest = False
while end_of_contest == False:
    data_input = input().split(":")

    if data_input[0] == "end of contests":
        end_of_contest = True
    else:
        contests_and_passwords[data_input[0]] = data_input[1]

end_of_submissions = False
while end_of_submissions == False:
    data_input = input().split("=>")

    if data_input[0] == "end of submissions":
        end_of_submissions = True
    else:
        contest = data_input[0]
        password = data_input[1]
        username = data_input[2]
        points = int(data_input[3])
        if valid_contest(contest) and valid_password(contest, password):
            create_username_if_does_not_exist(username)
            add_points_if_higher(contest, username, points)

users_and_contests = dict(sorted(users_and_contests.items()))

for username, contest_data in users_and_contests.items():
    users_and_total_points[username] = 0
    contest_data = dict(sorted(contest_data.items(), key=lambda item: item[1], reverse=True))
    users_and_contests[username] = contest_data
    for points in contest_data.values():
        users_and_total_points[username] += points
    if users_and_total_points[username] > user_max_points:
        user_max_points = users_and_total_points[username]
        user_with_max_points = username

print(f"Best candidate is {user_with_max_points} with total {user_max_points} points.")
print(f"Ranking:")

for username, contest_data in users_and_contests.items():
    print(f"{username}")
    for contest, points in contest_data.items():
        print(f"#  {contest} -> {points}")

# 02. Judge


contest_and_users = {}          #   {"contest1": {"user1": points, "user2": points}, "contest2": ...
users_and_total_points = {}     #   {"user1": total_points, "user2": total_points...

while True:
    user_input = input()

    if user_input == "no more time":
        break

    username, contest, points = user_input.split(" -> ")

    if contest not in contest_and_users.keys():
        contest_and_users[contest] = {}

    if username not in contest_and_users[contest].keys():
        contest_and_users[contest][username] = int(points)
        users_and_total_points[username] = 0
    else:
        contest_and_users[contest][username] = max(contest_and_users[contest][username], int(points))

# Sort inner dictonaries by points and then (if equal points) by username
# Then, as we're in a loop, gather each users' points and add them to the 'total_points' dictionary
for contest, contest_data in contest_and_users.items():
    sorted_data = {value[0] : value[1] for value in sorted(contest_data.items(), key = lambda x: (-x[1], x[0]))}
    contest_and_users[contest] = sorted_data
    for user, points in contest_and_users[contest].items():
        users_and_total_points[user] += points

# Sort the dictionary with users and total points
users_and_total_points = {value[0] : value[1] for value in sorted(users_and_total_points.items(), key = lambda x: (-x[1], x[0]))}

# Print contest and participants
for contest, contest_data in contest_and_users.items():
    print(f"{contest}: {len(contest_and_users[contest])} participants")
    counter = 1
    for user, points in contest_data.items():
        print(f"{counter}. {user} <::> {points}")
        counter += 1

# Print individual stats
print(f"Individual standings:")
counter = 1
for user, total_points in users_and_total_points.items():
    print(f"{counter}. {user} -> {total_points}")
    counter += 1

# 03. MOBA Challenger

users_position_and_skill_level = {}     # {"user1": {"skill1": level, "skill2": level...
user_total_skill_level = {}             # {"user1": total_skill_points, "user2": total_skill_points...

while True:
    user_input = input()

    if user_input == "Season end":
        break

    if " -> " in user_input:
        user, position, skill_level = user_input.split(" -> ")

        if user not in users_position_and_skill_level.keys():
            users_position_and_skill_level[user] = {}
            user_total_skill_level[user] = 0

        if position not in users_position_and_skill_level[user]:
            users_position_and_skill_level[user][position] = 0

        if users_position_and_skill_level[user][position] < int(skill_level):
            user_total_skill_level[user] -= users_position_and_skill_level[user][position]
            users_position_and_skill_level[user][position] = int(skill_level)
            user_total_skill_level[user] += int(skill_level)
    elif " vs " in user_input:
        user1, user2 = user_input.split(" vs ")
        if user1 in users_position_and_skill_level.keys() and user2 in users_position_and_skill_level.keys():
            user1_positions = list(users_position_and_skill_level[user1].keys())
            user2_positions = list(users_position_and_skill_level[user2].keys())
            matching_positions = []
            for position in user1_positions:
                if position in user2_positions:
                    matching_positions.append(position)
            if len(matching_positions) > 0:
                user_lost = ""
                user1_total_skill = user_total_skill_level[user1]
                user2_total_skill = user_total_skill_level[user2]
                if user1_total_skill > user2_total_skill:
                    user_lost = user2
                elif user1_total_skill < user2_total_skill:
                    user_lost = user1
                elif user1_total_skill == user2_total_skill:
                    user1_position_skill = users_position_and_skill_level[user1][matching_positions[0]]
                    user2_position_skill = users_position_and_skill_level[user2][matching_positions[0]]
                    if user1_position_skill > user2_position_skill:
                        user_lost = user2
                    elif user1_position_skill < user2_position_skill:
                        user_lost = user1

                users_position_and_skill_level.pop(user_lost)
                user_total_skill_level.pop(user_lost)

# Sort the dictionary with users and skill points
user_total_skill_level = {value[0] : value[1] for value in sorted(user_total_skill_level.items(), key = lambda x: (-x[1], x[0]))}

# Sort the inner dictionaries of the main dictionary
# We won't sort the outer (by user) as we're going to print them according the order of the smaller (total points) dictionary
for users, skill_points in users_position_and_skill_level.items():
    sorted_data = {value[0] : value[1] for value in sorted(skill_points.items(), key = lambda x: (-x[1], x[0]))}
    users_position_and_skill_level[users] = sorted_data

for user, total_skill_points in user_total_skill_level.items():
    print(f"{user}: {total_skill_points} skill")
    for skill, points in users_position_and_skill_level[user].items():
        print(f"- {skill} <::> {points}")

# 04. Snow White

dwarf_hat_and_physics = {}      # {"dwarf_id_1": {"name": "name", "hat_color": "color", "physics": 100}, ...
                                # dwarf_id = {name}_{color}
colors_count = {}               # {"color": counter, ...}
dwarf_counter = 0
while True:
    user_input = input()

    if user_input == "Once upon a time":
        break

    name, color, physics = user_input.split(" <:> ")

    dwarf_uid = name + "_" + color

    if color not in colors_count.keys():
        colors_count[color] = 0

    if dwarf_uid not in dwarf_hat_and_physics.keys():
        dwarf_hat_and_physics[dwarf_uid] = {}
        dwarf_hat_and_physics[dwarf_uid]["dwarf_name"] = name
        dwarf_hat_and_physics[dwarf_uid]["hat_color"] = color
        dwarf_hat_and_physics[dwarf_uid]["physics"] = int(physics)
        dwarf_hat_and_physics[dwarf_uid]["dwarf_order"] = dwarf_counter
        colors_count[color] += 1
    else:
        if dwarf_hat_and_physics[dwarf_uid]["physics"] < int(physics):
            dwarf_hat_and_physics[dwarf_uid]["physics"] = int(physics)

    dwarf_counter += 1

for dwarf_uid, dwarf_properties in dwarf_hat_and_physics.items():
    for color, count in colors_count.items():
        if dwarf_properties["hat_color"] == color:
            dwarf_properties["color_priority"] = count

sorted_dwarfs = {}
sorted_dwarfs = dict(sorted(dwarf_hat_and_physics.items(), key=lambda x: (-x[1]["physics"], -x[1]['color_priority'], x[1]['dwarf_order'])))

for dwarf_uid, dwarf_properties in sorted_dwarfs.items():
    print(f"({dwarf_properties['hat_color']}) {dwarf_properties['dwarf_name']} <-> {dwarf_properties['physics']}")

# 05. Dragon Army

qty_inputs = int(input())
dragon_stats = {}
default_stats = {"damage": 45, "health": 250, "armor": 10}
average_stats = {}

def populate_the_dragons():
    dragon_type, name, damage, health, armor = input().split()

    if dragon_type not in dragon_stats.keys():
        dragon_stats[dragon_type] = {}

    if name not in dragon_stats[dragon_type].keys():
        dragon_stats[dragon_type][name] = dict(default_stats)

    if damage != "null":
        dragon_stats[dragon_type][name]["damage"] = int(damage)

    if health != "null":
        dragon_stats[dragon_type][name]["health"] = int(health)

    if armor != "null":
        dragon_stats[dragon_type][name]["armor"] = int(armor)

def sort_the_dragons():
    for dragon_type, dragon_properties in dragon_stats.items():
        dragon_stats[dragon_type] = dict(sorted(dragon_properties.items()))

def calculate_average():
    for dragon_type, dragon_properties in dragon_stats.items():
        total_damage = 0
        total_health = 0
        total_armor = 0
        for dragon_name, propertie in dragon_properties.items():
            total_damage += propertie["damage"]
            total_health += propertie["health"]
            total_armor += propertie["armor"]
        avg_damage = total_damage / len(dragon_properties)
        avg_health = total_health / len(dragon_properties)
        avg_armor = total_armor / len(dragon_properties)
        average_stats[dragon_type] = f"{avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f}"

def print_the_dragons():
    for dragon_type, dragon_properties in dragon_stats.items():
        print(f"{dragon_type}::({average_stats[dragon_type]})")
        for dragon_name, propertie in dragon_properties.items():
            print(f"-{dragon_name} -> damage: {propertie['damage']}, health: {propertie['health']}, armor: {propertie['armor']}")

for i in range(qty_inputs):
    populate_the_dragons()

sort_the_dragons()
calculate_average()
print_the_dragons()
