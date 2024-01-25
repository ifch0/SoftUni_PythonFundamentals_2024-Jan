# 01. Exchange Integers

input_a = int(input())
input_b = int(input())

print(f'Before:')
print(f'a = {input_a}')
print(f'b = {input_b}')

input_a, input_b = input_b, input_a

print(f'After:')
print(f'a = {input_a}')
print(f'b = {input_b}')

# 02. Prime Number Checker

input_number = int(input())

is_prime = True

for i in range(2, input_number):
    if input_number == i:
        break
    elif input_number % i == 0:
        is_prime = False
        break

print(f'{is_prime}')

# 03. Decrypting Messages

key_value = int(input())
qty_lines = int(input())

decrypted_string = ''

for i in range(qty_lines):
    input_char = input()

    char_value = ord(input_char)
    new_char_value = char_value + key_value
    new_char = chr(new_char_value)
    decrypted_string += new_char

print(f'{decrypted_string}')

# 04. Balanced Brackets

qty_lines = int(input())

is_balanced = True
open_bracket = False

for i in range(qty_lines):
    current_input = input()

    if current_input == '(':
        if open_bracket == True:
            is_balanced = False
        else:
            open_bracket = True
    elif current_input == ')':
        if open_bracket == False:
            is_balanced = False
        else:
            open_bracket = False
    else:
        pass

if is_balanced == True:
    print(f'BALANCED')
else:
    print(f'UNBALANCED')
