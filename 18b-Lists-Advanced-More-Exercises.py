# 01. Social Distribution

population_wealth = list(map(int, input().split(', ')))
minimum_wealth = int(input())

richest = lambda: population_wealth.index(max(population_wealth))

def redistribute_money(people_list, rich, poor):
    gap = minimum_wealth - people_list[poor]
    people_list[poor] += gap
    people_list[rich] -= gap

no_equal = False

if len(population_wealth) * minimum_wealth > sum(population_wealth):
    no_equal = True
else:
    for i in range(len(population_wealth)):
        while population_wealth[i] < minimum_wealth:
            redistribute_money(population_wealth, richest(), i)

if no_equal:
    print(f'No equal distribution possible')
else:
    print(population_wealth)

# 02. Take/Skip Rope

input_list = list(input())

num_list = [int(x) for x in input_list if x.isdigit()]
sym_list = [x for x in input_list if not x.isdigit()]

take_list = num_list[0::2]
skip_list = num_list[1::2]

result_list = []

take = lambda: result_list.append(sym_list.pop(0))
skip = lambda: sym_list.pop(0)

for i in range(len(take_list)):
    for every in range(take_list[i]):
        take()
    for every in range(skip_list[i]):
        try:
            skip()
        except:
            ValueError

output_list = ''.join(result_list)
print(output_list)

# 03. Kate's Way Out

maze_rows = int(input())

maze = []

for i in range(maze_rows):
    maze.append(list(input()))

maze_columns = len(maze[0])

# sample maze
# exit moves should be + 1 (kate should go outside the maze)
#
#       y0   y6
#    x0 ######
#       ##  k#
#       ## ###
#       ######
#    x5 ## ###
#
#       y0   y6
#    x0 ######
#       ##  k#
#       ## ###
#   x4  ## ###


move_right = lambda x, y: (x, y + 1)
move_down = lambda x, y: (x + 1, y)
move_left = lambda x, y: (x, y - 1)
move_up = lambda x, y: (x - 1, y)

def find_path_and_start(rows, columns):
    free = ' '
    start = 'k'
    for row in range(rows):
        for column in range(columns):
            if maze[row][column] == free:
                possible_path.append([row, column])
            elif maze[row][column] == start:
                possible_path.append([row, column])
                starting_position.extend([row, column])
                cp.extend([row, column])
            else:
                pass

def find_exit(rows, columns):
    maze_exit = ' '
    for column in range(columns):
        if maze[0][column] == maze_exit:
            finish_position.extend([0, column])
        elif maze[rows - 1][column] == maze_exit:
            finish_position.extend([rows-1, column])
    for row in range(rows):
        if maze[row][0] == maze_exit:
            finish_position.extend([row, 0])
        elif maze[row][columns - 1] == maze_exit:
            finish_position.extend([rows, column - 1])

def go_trough_the_maze(x, y):
    cp = [x, y]
    boundary.append(cp)
    #already_checked.append(cp)
    while len(boundary) > 0:
        cp = [x, y]

        if list(move_left(*cp)) in possible_path and list(move_left(*cp)) not in already_checked:
            backtrack_steps[move_left(*cp)] = x, y
            boundary.append(list(move_left(*cp)))

        if list(move_down(*cp)) in possible_path and list(move_down(*cp)) not in already_checked:
            backtrack_steps[move_down(*cp)] = x, y
            boundary.append(list(move_down(*cp)))

        if list(move_right(*cp)) in possible_path and list(move_right(*cp)) not in already_checked:
            backtrack_steps[move_right(*cp)] = x, y
            boundary.append(list(move_right(*cp)))

        if list(move_up(*cp)) in possible_path and list(move_up(*cp)) not in already_checked:
            backtrack_steps[move_up(*cp)] = x, y
            boundary.append(list(move_up(*cp)))

        x, y = boundary.pop()
        already_checked.append(cp)
        cp = [x, y]

starting_position = []
finish_position = []
# current possition
cp = []
boundary = []
already_checked = []
possible_path = []
backtrack_steps = {}

find_path_and_start(maze_rows, maze_columns)
find_exit(maze_rows, maze_columns)
go_trough_the_maze(*cp)

moves = len(backtrack_steps) + 1

if len(possible_path) == len(already_checked):
    print(f'Kate got out in {moves} moves')
else:
    print(f'Kate cannot get out')

# 04. Battle Ships

field_rows = int(input())

battlefield = []
attack_moves = []
kill_count = 0

for i in range(field_rows):
    battlefield.append(list(map(int, input().split(' '))))

attack_moves = [x for x in input().split(' ')]

for attack_move in attack_moves:
    coordinates = [int(x) for x in attack_move.split('-')]
    if battlefield[coordinates[0]][coordinates[1]] != 0:
        battlefield[coordinates[0]][coordinates[1]] -= 1
        if battlefield[coordinates[0]][coordinates[1]] == 0:
            kill_count += 1

print(kill_count)

# 05. Dots

matrix_rows = int(input())

matrix = []

#sample matrix
#       y0     y5
#    x0 . . - - -
#       . . - - -
#       - - - - -
#       - - - . .
#    x5 - - - . .

for i in range(matrix_rows):
    matrix.append(list(map(str, input().split(' '))))

move_right = lambda x, y: (x, y + 1)
move_down = lambda x, y: (x + 1, y)
move_left = lambda x, y: (x, y - 1)
move_up = lambda x, y: (x - 1, y)

#convert a dot "." to a dash "-"
def clean_dot(x, y):
    matrix[x][y] = '-'

#go through the matrix and mark every dot's coordinates
def find_dots(rows, columns):
    dot = '.'
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == dot:
                all_dots.append([row, column])
            else:
                pass

#starting with the given coordinates, find all connected dots
def check_block_size(x, y):
    cp = [x, y]
    boundary.append(cp)
    while len(boundary) > 0:

        if list(move_left(*cp)) in all_dots and list(move_left(*cp)) not in already_checked and list(move_left(*cp)) not in boundary:
            boundary.append(list(move_left(*cp)))

        if list(move_down(*cp)) in all_dots and list(move_down(*cp)) not in already_checked and list(move_down(*cp)) not in boundary:
            boundary.append(list(move_down(*cp)))

        if list(move_right(*cp)) in all_dots and list(move_right(*cp)) not in already_checked and list(move_right(*cp)) not in boundary:
            boundary.append(list(move_right(*cp)))

        if list(move_up(*cp)) in all_dots and list(move_up(*cp)) not in already_checked and list(move_up(*cp)) not in boundary:
            boundary.append(list(move_up(*cp)))

        x, y = boundary.pop()
        already_checked.append(cp)
        cp = [x, y]

#remove already counted dots from the original matrix, so we can start with another block
def clean_checked_elements():
    for each in already_checked[::-1]:
        clean_dot(*each)
        already_checked.pop()

# count all the dots in the matrix
total_dots = 0
for i in range(matrix_rows):
    for j in matrix[i]:
        if j == '.':
            total_dots += 1

# cp = current position
cp = []

#neighbour cells we can check
boundary = []

#checked cells
already_checked = []

#list with sizes of the found blocks
connected_blocks_size = [0]

#main part
while total_dots != sum(connected_blocks_size):
    matrix_columns = len(matrix[0])
    #list with all dots's coordinates
    all_dots = []
    #find all possible dots
    find_dots(matrix_rows, matrix_columns)
    cp = all_dots[0]
    check_block_size(*cp)
    connected_blocks_size.append(len(already_checked))
    clean_checked_elements()

#print the largest block size
print(max(connected_blocks_size))
