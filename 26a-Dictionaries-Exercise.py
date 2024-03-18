# 01. Count Chars in a String

input_string = input()
input_data = [char for char in input_string if char != " "]
counter_dict = {}

for char in input_data:
    if char not in counter_dict:
        counter_dict[char] = 0
    counter_dict[char] += 1

for char, count in counter_dict.items():
    print(f"{char} -> {count}")

# 02. A Miner Task

resources_dict = {}

while True:
    input_resource = input()
    if input_resource == "stop":
        break
    input_qty = int(input())
    if input_resource not in resources_dict:
        resources_dict[input_resource] = 0
    resources_dict[input_resource] += input_qty

for resource, qty in resources_dict.items():
    print(f"{resource} -> {qty}")

# 03. Capitals

# ugly but works
#output_dict = dict(zip(input().split(", "), input().split(", ")))

countries = input().split(", ")
capitals = input().split(", ")

#works using zip
#output_dict = dict(zip(countries, capitals))

output_dict = {countries[i]: capitals[i] for i in range(len(countries))}

for country, capital in output_dict.items():
    print(f"{country} -> {capital}")

# 04. Phonebook

input_data = input()
phonebook = {}

while "-" in input_data:
    name, phone_number = input_data.split("-")
    phonebook[name] = phone_number
    input_data = input()

counter = int(input_data)

for i in range(counter):
    search_term = input()

    if search_term in phonebook:
        print(f"{search_term} -> {phonebook[search_term]}")
    else:
        print(f"Contact {search_term} does not exist.")

# 05. Legendary Farming

valuable_materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_material = ""
junk_materials = {}
item_found = False

def print_items(dictionary_to_print):
    for material, qty in dictionary_to_print.items():
        print(f"{material}: {qty}")

while item_found == False:
    input_items = input().split()

    for i in range(0, len(input_items), 2):
        material = input_items[i+1].lower()
        qty = int(input_items[i])

        if material in valuable_materials:
            valuable_materials[material] += qty
            if valuable_materials[material] >= 250:
                valuable_materials[material] -= 250
                key_material = material
                item_found = True
                break
        else:
            if material not in junk_materials:
                junk_materials[material] = 0
            junk_materials[material] += qty

print(f"{legendary_items[key_material]} obtained!")
print_items(valuable_materials)
print_items(junk_materials)

# 06. Orders

products = {}

def calculate(price, qty):
    return price * qty

input_data = input()
while input_data != "buy":
    item, price, qty = input_data.split()

    if item not in products:
        products[item] = {"price": float(price), "qty": int(qty)}
    else:
        products[item]["price"] = float(price)
        products[item]["qty"] += int(qty)

    input_data = input()

for product, data in products.items():
    print(f"{product} -> {calculate(data['price'], data['qty']):.2f}")

# 07. SoftUni Parking

qty_inputs = int(input())

users_and_plates = {}

def register(username, license_plate):
    if username not in users_and_plates.keys():
        users_and_plates[username] = license_plate
        print(f"{username} registered {license_plate} successfully")
    else:
        print(f"ERROR: already registered with plate number {users_and_plates[username]}")

def unregister(username):
    if username in users_and_plates.keys():
        users_and_plates.pop(username)
        print(f"{username} unregistered successfully")
    else:
        print(f"ERROR: user {username} not found")

def print_all():
    for user, plate in users_and_plates.items():
        print(f"{user} => {plate}")

for i in range(qty_inputs):
    split_input = input().split()

    if split_input[0] == "register":
        register(split_input[1], split_input[2])
    elif split_input[0] == "unregister":
        unregister(split_input[1])
    else:
        pass

print_all()

# 08. Courses

courses_and_students = {}

end = False

def print_all():
    for course, students in courses_and_students.items():
        print(f"{course}: {len(students)}")
        for student in students:
            print(f"-- {student}")

while end == False:
    input_data = input().split(" : ")

    if input_data[0] == "end":
        end = True
        break
    elif input_data[0] not in courses_and_students:
        courses_and_students[input_data[0]] = []
    courses_and_students[input_data[0]].append(input_data[1])

print_all()

# 09. Student Academy

qty_inputs = int(input())

students_and_grades = {}
selected_students = {}

for i in range(qty_inputs):
    student = input()
    grade = float(input())

    if student not in students_and_grades.keys():
        students_and_grades[student] = []
    students_and_grades[student].append(grade)

for student, grades in students_and_grades.items():
    average = sum(grades) / len(grades)
    if average >= 4.5:
        selected_students[student] = average

for student, average in selected_students.items():
    print(f"{student} -> {average:.2f}")

# 10. Company Users

companies_and_ids = {}

end = False
while end == False:
    input_data = input().split(" -> ")

    if input_data[0] == "End":
        end = True
        break

    if input_data[0] not in companies_and_ids.keys():
        companies_and_ids[input_data[0]] = []

    if input_data[1] not in companies_and_ids[input_data[0]]:
        companies_and_ids[input_data[0]].append(input_data[1])

for company, ids in companies_and_ids.items():
    print(f"{company}")
    for id in ids:
        print(f"-- {id}")

# 11. Force Book
# 90/100

force_and_users = {}

def create_side_if_no_such(side):
    if side not in force_and_users.keys():
        force_and_users[side] = []

def in_the_dictionary(user):
    found_in_any_force_side = False
    force_side = "None"
    for side, users in force_and_users.items():
        if user in users:
            found_in_any_force_side = True
            force_side = side

    return found_in_any_force_side, side

def add_user(user, side, command="add"):
    create_side_if_no_such(side)
    does_exist, force_side = in_the_dictionary(user)
    if not does_exist:
        force_and_users[side].append(user)
    elif does_exist and command == "change":
        users_to_manipulate = force_and_users[force_side]
        users_to_manipulate.remove(user)
        force_and_users[side].append(user)

    if command == "change":
        print(f"{user} joins the {side} side!")

def print_all():
    for force_side, users in force_and_users.items():
        if len(users) > 0:
            print(f"Side: {force_side}, Members: {len(users)}")
            for user in users:
                print(f"! {user}")

end = False
while end == False:
    input_data = input()
    if input_data == "Lumpawaroo":
        end = True
        break
    command = ""
    if "|" in input_data:
        command = "add"
        input_data = input_data.split(" | ")
        add_user(input_data[1], input_data[0], command)
    elif "->" in input_data:
        command = "change"
        input_data = input_data.split(" -> ")
        add_user(input_data[0], input_data[1], command)

print_all()

# 12. SoftUni Exam Results

exam_points = {}

end = False

while end == False:
    input_data = input().split("-")

    if input_data[0] == "exam finished":
        end = True
    elif input_data[1] == "banned":
            for courses, students in exam_points.items():
                if input_data[0] in students:
                    students.pop(input_data[0])
    else:
        student_name = input_data[0]
        course = input_data[1]
        grade = input_data[2]

        if course not in exam_points.keys():
            exam_points[course] = {}
            exam_points[course]["Submissions"] = 0

        exam_points[course]["Submissions"] += 1

        if student_name not in exam_points[course].keys():
            exam_points[course][student_name] = int(grade)
        else:
            if exam_points[course][student_name] < int(grade):
                exam_points[course][student_name] = int(grade)

print("Results:")
for course, grades_data in exam_points.items():
    for student_name, grade in grades_data.items():
        if student_name != "Submissions":
            print(f"{student_name} | {grade}")
print("Submissions:")
for course, grades_data in exam_points.items():
    for submission, count in grades_data.items():
        if submission == "Submissions":
            print(f"{course} - {count}")
