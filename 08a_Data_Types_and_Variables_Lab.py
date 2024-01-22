# 01. Concat Names

first_name = input()
last_name = input()
delimiter = input()

print(f'{first_name}{delimiter}{last_name}')

# 02. Convert Meters to Kilometers

in_meters = int(input())

out_kilometers = in_meters / 1000

print(f'{out_kilometers:.2f}')

# 03. Pounds to Dollars

gbp = int(input())

usd_to_gbp = 1.31

usd = gbp * usd_to_gbp

print(f'{usd:.3f}')

# 04. Centuries to Minutes

in_centuries = int(input())

days_in_year = 365.2422

out_years = in_centuries * 100
out_days = int(out_years * days_in_year)
out_hours = out_days * 24
out_minutes = out_hours * 60

print(f'{in_centuries} centuries = {out_years} years = {out_days} days = {out_hours} hours = {out_minutes} minutes')

# 05. Special Numbers

input_number = int(input())

for number in range(1, input_number + 1):
    special = False
    digit_sum = 0
    current_string = str(number)
    for digit in current_string:
        digit_sum += int(digit)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        special = True
    print(f'{number} -> {special}')

# 06. Next Happy Year

input_year = int(input())
happy_year = input_year
found_next_year = False

while found_next_year == False:
    happy_year += 1
    if len(str(happy_year)) == len(set(str(happy_year))):
        found_next_year = True

print(f'{happy_year}')
