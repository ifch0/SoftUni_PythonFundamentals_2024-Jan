# 01. Reverse Strings

while True:
    user_input = input()

    if user_input == "end":
        break

    reversed_word = user_input[::-1]
    print(f"{user_input} = {reversed_word}")

# 02. Repeat Strings

input_strings = input().split()
output_string = ""

for string in input_strings:
    for iteration in range(len(string)):
        output_string += string

print(f"{output_string}")

# 03. Substring

substring = input()
whole_string = input()

while substring in whole_string:
    whole_string = whole_string.replace(substring, "")

print(f"{whole_string}")

# 04. Text Filter

ban_list = input().split(", ")
input_text = input()

for bad_word in ban_list:
    while bad_word in input_text:
        input_text = input_text.replace(bad_word, len(bad_word) * "*")

print(f"{input_text}")

# 05. Digits, Letters and Other

input_string = input()

output = ""
for char in input_string:
    if char.isnumeric():
        output += char
print(output)
output = ""
for char in input_string:
    if char.isalpha():
        output += char
print(output)
output = ""
for char in input_string:
    if char.isnumeric() == False and char.isalpha() == False:
        output += char
print(output)
