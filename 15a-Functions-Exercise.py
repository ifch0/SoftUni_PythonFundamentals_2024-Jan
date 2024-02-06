# 01. Smallest of Three Numbers

from math import inf

min_num = inf

def check_if_smaller(number, current_min):
    if number <= current_min:
        current_min = number

    return current_min

for i in range(3):
    num_check = int(input())
    min_num = check_if_smaller(num_check, min_num)

print(min_num)

# 02. Add and Subtract

sum_numbers = lambda a, b: a + b
subtract = lambda a, b: a - b

def add_and_subtract(num_a, num_b, num_c):
    addition_result = sum_numbers(num_a, num_b)
    subtract_result = subtract(addition_result, num_c)

    return subtract_result

num_a = int(input())
num_b = int(input())
num_c = int(input())

result = add_and_subtract(num_a, num_b, num_c)

print(result)

# 03. Characters in Range

def fill_the_string(start, stop):
    output_list = []
    for i in range(start+1, stop):
        output_list.append(chr(i))
    return output_list

start_chr = input()
stop_chr = input()

output_list = fill_the_string(ord(start_chr), ord(stop_chr))

print(*output_list, sep=' ')

# 04. Odd and Even Sum

input_string = input()

is_even = lambda x: x % 2 == 0

even_list = []
odd_list = []

for num in input_string:
    if is_even(int(num)):
        even_list.append(int(num))
    else:
        odd_list.append(int(num))

print(f'Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}')

# 05. Even Numbers

input_list = list(map(int, input().split(' ')))

is_even = lambda x: x % 2 == 0

even_list = []

for num in input_list:
    if is_even(num):
        even_list.append(int(num))

print(even_list)

# 06. Sort

input_list = list(map(int, input().split(' ')))

print(sorted(input_list))

# 07. Min Max and Sum

input_list = list(map(int, input().split(' ')))

print(f'The minimum number is {min(input_list)}')
print(f'The maximum number is {max(input_list)}')
print(f'The sum number is: {sum(input_list)}')

# 08. Palindrome Integers

input_list = list(map(str, input().split(', ')))

is_palindrome = lambda some_string: some_string == some_string[::-1]

for each in input_list:
    print(is_palindrome(each))

# 09. Password Validator

def length_check(some_string):
    if 6 <= len(some_string) <= 10:
        return True
    else:
        return False

def symbols_check(some_string):
    for symbol in some_string:
        if  48 <= ord(symbol) <= 57 or 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122:
            pass
        else:
            return False
    return True

def qty_digits_check(some_string):
    digit_counter = 0
    for symbol in some_string:
        if 48 <= ord(symbol) <= 57:
            digit_counter += 1
            if digit_counter >= 2:
                return True
    return False

password_to_check = input()

length = length_check(password_to_check)
symbols = symbols_check(password_to_check)
qty_digits = qty_digits_check(password_to_check)

if not length:
    print(f'Password must be between 6 and 10 characters')
if not symbols:
    print(f'Password must consist only of letters and digits')
if not qty_digits:
    print(f'Password must have at least 2 digits')

if length and symbols and qty_digits:
    print(f'Password is valid')

# 10. Perfect Number

integer_to_check = int(input())

divisors_list = []

for i in range(1, integer_to_check):
    if integer_to_check % i == 0:
        divisors_list.append(i)

if integer_to_check == sum(divisors_list):
    print(f'We have a perfect number!')
else:
    print(f'It\'s not so perfect.')

# 11. Loading Bar

input_integer = int(input())

print()

def loading_bar(percent):
    output = ''
    for i in range(int(percent/10)):
        output += '%'

    return output

if input_integer < 100:
    print(f'{input_integer}% [{loading_bar(input_integer).ljust(10, ".")}]')
    print(f'Still loading...')
else:
    print(f'100% Complete!')
    print(f'[{loading_bar(input_integer)}]')

# 12. Factorial Division

from math import factorial

input_a = int(input())
input_b = int(input())

result = factorial(input_a) / factorial(input_b)

print(f'{result:0.2f}')

# 12. Factorial Division (version 2)

input_a = int(input())
input_b = int(input())

def factorial_calculation(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

division_result = factorial_calculation(input_a) / factorial_calculation(input_b)

print(f'{division_result:0.2f}')
