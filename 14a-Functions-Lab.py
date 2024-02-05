# 01. Absolute Values

list_input = list(map(float, input().split(' ')))
output_list = []

def abs_values(work_list):
    temp_list = []
    for i in range(len(work_list)):
        temp_list.append(abs(work_list[i]))

    return temp_list

output_list = abs_values(list_input)
print(output_list)es(list_input)
print(output_list)

# 02. Grades

input_grade = float(input())

def grade_to_words(grade):
    if 2 <= grade < 3:
        return 'Fail'
    elif 3 <= grade < 3.5:
        return 'Poor'
    elif 3.5 <= grade < 4.5:
        return 'Good'
    elif 4.5 <= grade < 5.5:
        return 'Very Good'
    elif 5.5 <= grade <= 6.00:
        return 'Excellent'
    else:
        pass

result = grade_to_words(input_grade)
print(result)

# 03. Calculations

user_command = input()
num_a = int(input())
num_b = int(input())

def multiply(a, b):
    return a * b

def divide(a, b):
    return int(a / b)

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a- b

result = 0

if user_command == 'multiply':
    result = multiply(num_a, num_b)
elif user_command == 'divide':
    result = divide(num_a, num_b)
elif user_command == 'add':
    result = addition(num_a, num_b)
elif user_command == 'subtract':
    result = subtraction(num_a, num_b)

print(result)

# 04. Repeat String

string_input = input()
count = int(input())

def text_repeat(string, counter):
    return string * counter

result = text_repeat(string_input, count)

print(result)

# 05. Orders

product_type = input()
product_qty = int(input())

def price_calculation(product, quantity):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'water':
        return quantity * 1
    elif product == 'coke':
        return quantity * 1.4
    elif product == 'snacks':
        return quantity * 2
    else:
        pass

total_price = price_calculation(product_type, product_qty)

print(f'{total_price:0.2f}')

# 06. Calculate Rectangle Area

input_w = int(input())
input_h = int(input())

def calc_area(width, height):
    return width * height

area = calc_area(input_w, input_h)

print(area)

# 07. Rounding

num_input = list(map(float, input().split(' ')))

def round_num(number):
    return round(number)

result = []

for each in num_input:
    result.append(round_num(each))

print(result)
