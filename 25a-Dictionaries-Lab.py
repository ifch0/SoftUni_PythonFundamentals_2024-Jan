# 01. Bakery

input_elements = input().split(" ")
ingredient_dict = {}

for i in range(0, len(input_elements), 2):
    key = input_elements[i]
    value = input_elements[i+1]
    ingredient_dict[key] = int(value)

print(ingridient_dict)

# 02. Stock

input_elements = input().split(" ")
search_elements = input().split(" ")

ingredient_dict = {}

for i in range(0, len(input_elements), 2):
    key = input_elements[i]
    value = input_elements[i+1]
    ingredient_dict[key] = int(value)

for each in search_elements:
    if each in ingredient_dict.keys():
        print(f"We have {ingredient_dict[each]} of {each} left")
    else:
        print(f"Sorry, we don't have {each}")

# 03 Statistics

stock = {}
input_elements = input().split(": ")

while input_elements[0] != "statistics":
    if input_elements[0] not in stock.keys():
        stock[input_elements[0]] = int(input_elements[1])
    else:
        stock[input_elements[0]] += int(input_elements[1])

    input_elements = input().split(": ")

print(f"Products in stock:")

for item, qty in stock.items():
    print(f"- {item}: {qty}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")

# 04. Students

students = {}
input_data = input()

while ":" in input_data:
    split_data = input_data.split(":")
    if split_data[2] not in students:
        students[split_data[2]] = {split_data[1]: split_data[0]}
    else:
        students[split_data[2]][split_data[1]] = split_data[0]

    input_data = input()

search_term = " ".join(input_data.split("_"))
selected_course = students[search_term]

for id, name in selected_course.items():
    print(f"{name} - {id}")

# 05. ASCII Values

input_data = input().split(", ")

ascii_dict = {x: ord(x) for x in input_data}

print(ascii_dict)

# 06. Odd Occurrences

input_data = input().split(" ")
counter_dict = {}
output_list = []

for item in input_data:
    if item.lower() not in counter_dict:
        counter_dict[item.lower()] = 0
    counter_dict[item.lower()] += 1

for key, value in counter_dict.items():
    if value %2 != 0:
        output_list.append(key)

print(*output_list)

# 07. Word Synonyms

iterations = int(input())
synonym_dict = {}

for i in range(iterations):
    key = input()
    value = input()

    if key not in synonym_dict:
        synonym_dict[key] = []
    synonym_dict[key].append(value)

for key, value in synonym_dict.items():
    word = key
    synonyms = ", ".join(value)
    print(f"{word} - {synonyms}")
