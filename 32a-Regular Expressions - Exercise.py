# 01. Capture the Numbers

import re

pattern = r'\d+'

user_input = input()
while user_input:
    matches = re.findall(pattern, user_input)
    if matches:
        print(" ".join(matches), end= " ")
    user_input = input()

# 02. Find Variable Names in Sentences

import re

pattern = r'\b_([a-zA-Z0-9]+)\b'

user_input = input()
matches = re.findall(pattern, user_input)
if matches:
    print(",".join(matches))

# 03. Find Occurrences of Word in Sentence

import re

input_string = input()
search_string = input()

pattern = fr"(?i)\b{search_string}\b"

matches = re.findall(pattern, input_string)

print(len(matches))

# 04. Extract Emails

import re

input_string = input()

pattern = r"\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"

matches = re.findall(pattern, input_string)

for each in matches:
    print(each[0])

# 05. Furniture

import re

pattern = r">>([a-zA-z]+)<<((\d+)(\.\d+)?)!(\d+)"

bought_items = []
total_price = 0

while True:
    user_input = input()
    if user_input == "Purchase":
        break
    else:
        matches = re.findall(pattern, user_input)
        if matches:
            type = matches[0][0]
            item_price = float(matches[0][1])
            qty = int(matches[0][4])
            bought_items.append(type)
            total_price += item_price * qty

print(f"Bought furniture:")
for item in bought_items:
    print(item)
print(f"Total money spend: {total_price:.2f}")

# 06. Extract the Links

import re

pattern = r"((www\.)([a-zA-Z0-9\-]+)((\.[a-z]+)+))"

user_input = input()
while user_input:
    matches = re.findall(pattern, user_input)
    if matches:
        print(matches[0][0])
    user_input = input()
