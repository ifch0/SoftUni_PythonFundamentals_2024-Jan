# 01. SoftUni Reception

employee_efficiency = []

for i in range(3):
    employee_efficiency.append(int(input()))

qty_students = int(input())

efficiency_per_hour = sum(employee_efficiency)

hours_counter = 0
lunch_break = 0

while qty_students > efficiency_per_hour:
    hours_counter += 1
    qty_students -= efficiency_per_hour
    if hours_counter % 3 == 0:
        lunch_break += 1

if qty_students > 0:
    hours_counter += 1

total_hours = hours_counter + lunch_break

print(f'Time needed: {total_hours}h.')

# 02. Array Modifier

array_input = list(map(int, input().split()))

def cmd_swap(index_1, index_2):
    array_input[index_1], array_input[index_2] = array_input[index_2], array_input[index_1]

def cmd_multiply(index_1, index_2):
    array_input[index_1] *= array_input[index_2]

def cmd_decrease():
    for i in range(len(array_input)):
        array_input[i] -= 1

end = False
while end == False:
    command_input = input().split()

    if command_input[0] == 'end':
        end = True
    elif command_input[0] == 'swap':
        cmd_swap(int(command_input[1]), int(command_input[2]))
    elif command_input[0] == 'multiply':
        cmd_multiply(int(command_input[1]), int(command_input[2]))
    elif command_input[0] == 'decrease':
        cmd_decrease()
    else:
        pass

output = ', '.join(str(x) for x in array_input)
print(output)

# 03. Numbers

array_input = list(map(int, input().split()))

average = sum(array_input) / len(array_input)

above_average = []

for i in array_input:
    if i > average:
        above_average.append(i)

if len(above_average) == 0:
    print(f'No')
else:
    above_average.sort(reverse=True)
    del above_average[5:]
    print(*above_average)
