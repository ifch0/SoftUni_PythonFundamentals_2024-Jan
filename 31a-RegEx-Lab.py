# 01. Match Full Name

import re

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

user_input = input()

matches = re.findall(pattern, user_input)

print(" ".join(matches))

# 02. Match Phone Number

import re

pattern = r'\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b'

user_input = input()

matches = re.findall(pattern, user_input)

print(", ".join(matches))

# 03. Match Dates

import re

pattern = r'(\d{2})(\.|-|/)([A-Z][a-z]{2})\2(\d{4})'

user_input = input()

matches = re.findall(pattern, user_input)

for match in matches:
    day = match[0]
    month = match[2]
    year = match[3]

    print(f"Day: {day}, Month: {month}, Year: {year}")

# 04. Match Numbers

import re

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

user_input = input()

matches = re.finditer(pattern, user_input)

for match in matches:
    print(match.group(), end=" ")
