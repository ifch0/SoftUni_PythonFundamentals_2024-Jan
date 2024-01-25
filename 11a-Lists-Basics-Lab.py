# 01. Strange Zoo

tail = input()
body = input()
head = input()

animal = [tail, body, head]

animal[0], animal[2] = animal[2], animal[0]

print(animal)

# 02. Courses

qty_courses = int(input())

courses = []

for course in range(qty_courses):
    course_name = input()
    courses.append(course_name)

print(courses)

# 03. List Statistics

qty_inputs = int(input())

positive_list = []
negative_list = []

for i in range(qty_inputs):
    user_input = int(input())

    if user_input >= 0:
        positive_list.append(user_input)
    else:
        negative_list.append(user_input)

print(positive_list)
print(negative_list)
print(f'Count of positives: {len(positive_list)}')
print(f'Sum of negatives: {sum(negative_list)}')

# 04. Search

qty_inputs = int(input())
search_word = input()

list_with_strings = []
filtered_list = []

for i in range(qty_inputs):
    user_input = input()

    list_with_strings.append(user_input)

for i in range(len(list_with_strings)):
    current_element = list_with_strings[i]
    if search_word in current_element:
        filtered_list.append(current_element)

print(list_with_strings)
print(filtered_list)

# 05. Numbers Filter

qty_inputs = int(input())

full_list = []
filtered_list = []

for i in range(qty_inputs):
    current_input = int(input())
    full_list.append(current_input)

filter_criteria = input()

for i in range(len(full_list)):
    if full_list[i] % 2 == 0 and filter_criteria == 'even':
        filtered_list.append(full_list[i])
    elif full_list[i] % 2 != 0 and filter_criteria == 'odd':
        filtered_list.append(full_list[i])
    elif full_list[i] < 0 and filter_criteria == 'negative':
        filtered_list.append(full_list[i])
    elif full_list[i] >= 0 and filter_criteria == 'positive':
        filtered_list.append(full_list[i])
    else:
        pass

print(filtered_list)
