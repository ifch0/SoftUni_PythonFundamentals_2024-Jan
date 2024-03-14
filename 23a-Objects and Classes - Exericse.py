# 01. Storage

class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage

storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())

# 02. Weapon

class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return f"shooting..."
        else:
            return f"no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)

# 03. Catalogue

class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        output_list = [x for x in self.products if x.startswith(first_letter)]
        return output_list

    def __repr__(self):
        output_string = f"Items in the {self.name} catalogue:\n"
        output_string += "\n".join(sorted(self.products))
        return output_string

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

# 04. Town

class Town:
    def __init__(self, name: str):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        #output_string = f"Town: {self.name} | Latitude {self.latitude} | Longitude {self.longitude}"
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)

# 05. Class

class Class:
    __students_count = 22
    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return average_grade

    def __repr__(self):
        average_grade = self.get_average_grade()
        students = ", ".join(self.students)
        output_string = f"The students in {self.name}: {students}. Average grade: {average_grade:.2f}"
        return output_string

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)

# 06. Inventory

class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        items = ", ".join(self.items)
        capacity_left = self.__capacity - len(self.items)
        output_string = f"Items: {items}.\nCapacity left: {capacity_left}"
        return output_string

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

# 07. Articles

class Article:
    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str):
        self.content = new_content

    def change_author(self, new_author: str):
        self.author = new_author

    def rename(self, new_title: str):
        self.title = new_title

    def __repr__(self):
        output_string = f"{self.title} - {self.content}: {self.author}"
        return output_string

article = Article("Highest Recorded Temperature", "Temperatures across Europe are unprecedented, according to scientists.", "Ben Turner")
article.edit("Syracuse, a city on the coast of the Italian island of Sicily, registered temperatures of 48.8 degrees Celsius")
article.rename("Temperature in Italy")
article.change_author("B. T.")
print(article)

# 08. Vehicle

class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and not self.owner:
            self.owner = owner
            change = money - self.price
            output_string = f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif self.owner:
            output_string = f"Car already sold"
        elif money < self.price:
            output_string = f"Sorry, not enough money"
        return output_string

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return (f"Vehicle has no owner")

    def __repr__(self):
        if self.owner == None:
            output_string = f"{self.model} {self.type} is on sale: {self.price}"
        else:
            output_string = f"{self.model} {self.type} is owned by: {self.owner}"
        return output_string

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)

# 09. Movie 

class Movie:
    __watched_movies = 0
    
    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"
