# 01. Data Types

def func_int(some_int):
    return some_int * 2

def func_real(some_float):
    return f'{(some_float * 1.5):0.2f}'

def func_str(some_string):
    return '$' + some_string + '$'

command_input = input()
data_input = input()

if command_input == 'int':
    result = func_int(int(data_input))
elif command_input == 'real':
    result = func_real(float(data_input))
elif command_input == 'string':
    result = func_str(data_input)

print(result)

# 02. Center Point

from math import sqrt, floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def distance_to_center(x, y):
    return sqrt(x*x + y*y)

if distance_to_center(x1, y1) < distance_to_center(x2, y2):
    print(f'({floor(x1)}, {floor(y1)})')
else:
    print(f'({floor(x2)}, {floor(y2)})')

# 03. Longer Line (60/100)

from math import sqrt, floor

total_lines = 2

total_coordinates = []
line_lengths = []
longest_line_index = ''

def fill_coordinates(lines):
    all_coordinates = []
    for line in range(total_lines):
        lines = []
        for i in range(2):
            points = []
            points.append(float(input()))
            points.append(float(input()))
            lines.append(points)
        all_coordinates.append(lines)
    return all_coordinates

def distance_between_points(x1, y1, x2, y2):
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

def line_length(total_lines, all_coordinates):
    line_length = 0
    line_lengths = []
    for line in range(total_lines):
        line_length = distance_between_points(all_coordinates[line][0][0], all_coordinates[line][0][1], all_coordinates[line][1][0], all_coordinates[line][1][1])
        line_lengths.append(line_length)
    return line_lengths

def closest_point_to_center(line_index, all_coordinates):
    x_coordinates = f'({floor(all_coordinates[line_index][0][0])}, {floor(all_coordinates[line_index][0][1])})'
    y_coordinates = f'({floor(all_coordinates[line_index][1][0])}, {floor(all_coordinates[line_index][1][1])})'
    point_coordinates = [x_coordinates, y_coordinates]

    if distance_between_points(0, 0, all_coordinates[line_index][0][0], all_coordinates[line_index][0][1]) <= distance_between_points(0, 0, all_coordinates[line_index][1][0], all_coordinates[line_index][1][1]):
        return point_coordinates
    else:
        return point_coordinates[::-1]

def print_coordinates(points_coordinates_list):
    print(*points_coordinates_list, sep='')

total_coordinates = fill_coordinates(total_lines)
line_lengths = line_length(total_lines, total_coordinates)
longest_line_index = line_lengths.index(max(line_lengths))
longest_line_coordinates = closest_point_to_center(longest_line_index, total_coordinates)
print_coordinates(longest_line_coordinates)


# 04. Tribonacci Sequence

qty_prints = int(input())

temp_list = [0, 0, 1]
output_list = [1]

for i in range(qty_prints - 1):
    output_list.append(sum(temp_list))
    temp_list.append(sum((temp_list)))
    temp_list.pop(0)

print(*output_list)

# 05. Multiplication Sign

integers_input = []

for i in range(3):
    integers_input.append(int(input()))

negative_counter = 0
is_zero = False
is_negative = False

for i in range(len(integers_input)):
    if integers_input[i] == 0:
        is_zero = True
    if integers_input[i] < 0:
        negative_counter += 1

if negative_counter % 2 != 0:
    is_negative = True

if is_zero:
    print('zero')
elif is_negative:
    print('negative')
else:
    print('positive')
