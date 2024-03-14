# 01. Comment

class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

comment = Comment('user1', 'I like this book')
print(comment.username)
print(comment.content)
print(comment.likes)

# 02. Party

class Party:
    def __init__(self):
        self.people = []

party = Party()
line = input()

while line != 'End':
    party.people.append(line)
    line = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")

# 03. Email

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

separate_emails = []

while True:
    input_line = input()

    if input_line == 'Stop':
        break
    else:
        input_strings = input_line.split(' ')
        sender = input_strings[0]
        receiver = input_strings[1]
        mail_body = input_strings[2]
        email = Email(sender, receiver, mail_body)
        separate_emails.append(email)

send_emails = list(map(int, input().split(', ')))

for x in send_emails:
    separate_emails[x].send()

for email in separate_emails:
    print(email.get_info())


# 04. Zoo

class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal):
        if species == 'mammal':
            self.mammals.append(animal)
        elif species == 'fish':
            self.fishes.append(animal)
        elif species == 'bird':
            self.birds.append(animal)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == 'mammal':
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {my_zoo.__animals}"
        return result

my_zoo_name = input()
my_zoo = Zoo(my_zoo_name)

iterations = int(input())

for i in range(iterations):
    animal = input().split(" ")
    my_zoo.add_animal(animal[0], animal[1])

species_to_check = input()
print(my_zoo.get_info(species_to_check))


# 05. Circle

class Circle:
    __pi = 3.14
    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.__pi * self.diameter

    def calculate_area(self):
        return self.__pi * (0.5 * self.diameter) * (0.5 * self.diameter)

    def calculate_area_of_sector(self, angle):
        whole_area = self.calculate_area()
        sector_area = angle / 360 * whole_area
        return sector_area

circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
