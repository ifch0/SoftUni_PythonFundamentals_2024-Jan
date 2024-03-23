# 01. Extract Person Information

qty_inputs = int(input())

for i in range(qty_inputs):
    input_string = input()

    name_start = input_string.index("@")
    name_end = input_string.index("|")
    age_start = input_string.index("#")
    age_end = input_string.index("*")

    name = input_string[name_start+1:name_end]
    age = input_string[age_start+1:age_end]

    print(f"{name} is {age} years old.")

# 02. ASCII Sumator

start_char = input()
end_char = input()
string_input = input()
output_sum = 0

for char in string_input:
    if ord(start_char) < ord(char) < ord(end_char):
        output_sum += ord(char)

print(output_sum)

# 03. Treasure Finder

key_sequence = [int(x) for x in input().split()]

key_counter_max = len(key_sequence)
decrypted_messages = []
while True:
    string_input = input()
    if string_input == "find":
        break
    key_counter = 0
    output_string = ""
    for char in string_input:
        new_char = chr(ord(char) - key_sequence[key_counter])
        output_string += new_char
        key_counter += 1
        if key_counter == key_counter_max:
            key_counter = 0
    decrypted_messages.append(output_string)

for message in decrypted_messages:
    treasure_start = message.index("&") +1
    treasure_end = message.index("&", treasure_start +1)
    coordinates_start = message.index("<") +1
    coordinates_end = message.index(">")

    treasure_type = message[treasure_start:treasure_end]
    coordinates = message[coordinates_start:coordinates_end]

    print(f"Found {treasure_type} at {coordinates}")

# 04. Morse Code Translator

morse_code_dict = {".-": "A", "-...": "B", "-.-.": "C",  "-..": "D", ".": "E",
                   "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
                   "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
                   ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
                   "..-": "U", "...-": "V", ".--": "W", "-..-": "X","-.--": "Y", "--..": "Z",
                   "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
                   ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"}

input_code = input()
output_string = ""
words = input_code.split("|")

for word in words:
    letters = word.split()

    for letter in letters:
        char = morse_code_dict[letter]
        output_string += char

    output_string += " "

print(output_string)

# 05. HTML

header = input()
article = input()
comments = []

while True:
    user_input = input()

    if user_input == "end of comments":
        break

    comments.append(user_input)

print(f"<h1>")
print(f"\t{header}")
print(f"</h1>")

print(f"<article>")
print(f"\t{article}")
print(f"</article>")

for comment in comments:
    print(f"<div>")
    print(f"\t{comment}")
    print(f"</div>")
