# 01. Number Definer

number = float(input())

if number == 0:
    print('zero')
elif abs(number) < 1:
    print('small ', end='')
elif abs(number) > 1000000:
    print('large ', end='')
else:
    pass

if number < 0:
    print('negative')
elif number > 0:
    print('positive')
else:
    pass

