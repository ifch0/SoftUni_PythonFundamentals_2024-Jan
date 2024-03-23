input_string = input()
input_string = input_string.replace(",", " ")
tickets = input_string.split()
winning_chars = ["@", "#", "$", "^"]

def valid(ticket):
    if len(ticket) == 20:
        return True
    print(f"invalid ticket")

def is_winning(ticket):
    first_half = ticket[:10]
    second_half = ticket[10:]
    for counter in range(10, 5, -1):
        for winning_char in winning_chars:
            if winning_char * counter * 2 in ticket:
                return f"{counter}{winning_char} Jackpot!"
            if winning_char * counter in first_half and winning_char * counter in second_half:
                return f"{counter}{winning_char}"
    return "no match"

for ticket in tickets:
    if valid(ticket):
        output = is_winning(ticket)
        print(f'ticket "{ticket}" - {output}')
