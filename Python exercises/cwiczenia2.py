# Create a dictionary that describes a person's contact information. Print name and phone number as one string with explanation. For example:
# “Bob Dylan, phone number: 000-000-000”
from typing import Any

print("Exercise 8")

dictionary1 = {
    'Name': 'Tomasz Nowak',
    'Phone number': "111 - 222 - 333"
}
dictionary2 = {
    'Name': 'Piotr Kowalski',
    'Phone number': "123 - 123 - 123"
}

#print(f"First: {dictionary1['Name']} phone number: {dictionary1['Phone number']}" '\n'
#      f"Second: {dictionary2['Name']} phone number: {dictionary2['Phone number']}")

for i in [dictionary1, dictionary2]:
    print(f" Name: {i['Name']}, phone number: {i['Phone number']}")

# Create a list of  dictionaries that describe a worker (his name/surname, position, project etc). Print one of the worker’s information.
# There is a string that describes employee information, e.g.:
# “Lilly;Brown;QA Engineer;Samsung”
# List values are separated with “;”.
# Print out a string that represents name, surname, position and project from the given string with explanation. For example:
# Name: Lilly, Surname: Brown. Position: QA Engineer, project: Samsung.
# Note: you can use list indexes to form the output string.

print("Exercise 9")

list = [{
    'Name': 'Lilly',
    'Surname': 'Brown',
    'Position': 'QA Engineer',
    'Project': 'Samsung'
},
    {'Name': 'Bob',
    'Surname': 'Doe',
    'Position': 'Project Manager',
    'Project': 'Nokia'

     }]

for i in list:
    print(f"Name: {i['Name']}; Surname: {i['Surname']}; Position: {i['Position']}; Project: {i['Project']}")



# You have a dictionary of dicitionaries:
# {
#     “Ford Fiesta”: {
#          “year”: 2014,
#          “color”: “Candy blue”
#     # },
#     “Seat Leon”: {
#          “year”: 2018,
#          “color”: “Desire red”
#     }
# }
#
# Form and print out the following string:
# “You picked ‘Seat Leon’. Selected color: ‘Desire red’, year of production: 2018”

print("Exercise 10")

car_list = {
    'Ford Fiesta': {
        'year': 2014,
        'color': 'Candy blue'
    },
    'Seat Leon': {
        'year': 2018,
        'color': 'Desire red'
    }
}

items = car_list['Seat Leon'].items()
print("You picked `Seat Leon`", end=' ')
for i in items:
    print(f"'{i[0]}': '{i[1]}'", end=', ')
print()

# Create a dictionary that describes your laptop technical details (e.g. RAM, hard drive capacity etc.) Using the
# get() method of dictionaries print out existing and missing information. You should use get() at least once for
# each case: get(existing key) get(missing key) get(missing key, default value)

print("Exercise 11")

myLaptop = {
    'Name': 'Asus',
    'RAM': '8 GB',
    'Hard drive': '1 TB'
}

print(f"My laptop name:  {myLaptop.get('Name')}. My laptop RAM: {myLaptop.get('RAM')}. My laptop weight: {myLaptop.get('weight')}. My laptop size: {myLaptop.get('Size', 'Default size 1')}.")


# You have a string: “My name is Bob”. Using [:], split() and append() methods, create a string that replaces Bob with your name.
print("Exercise 12")

originalText = "My name is Bob"
print(originalText.split())

changedText: Any = (originalText.split())[:3]
changedText.append("Karolina")

for i in changedText:
    print(i, end=" ")
print()

# Think about 7 favourite dishes that you like. Now, you have to create a schedule of eating them each day. Create a
# dictionary with 7 keys (names of week days). For each key the value will be a dictionary containing the name of
# your favourite dish and list of ingredients that you have to buy to cook it.

# Try to print out ingredients for different days of the week.

print("Exercise 13")
dishes = {
    'Monday': {
        'name': "jajecznica",
        'ingredients': ["jajko", "sol", "pieprz", "szczypiorek"]
    },
    'Tuesday': {
        'name': "tosty",
        'ingredients': ["chleb", "maslo", "szynka"]
    },
    'Wednesday': {
        'name': "kanapki",
        'ingredients': ["bulki", "margaryna", "ser"]
    },
    'Thursday': {
        'name': "owsianka",
        'ingredients': ["banan", "platki"]
    },
    'Friday': {
        'name': "kawa",
        'ingredients': ["ziarno", "woda", "mleko"]
    },
}

dishes_items = dishes.items()

#[
#    ('Monday', {'name': 'jajecznica', 'ingredients': ['jajko', 'sol', 'pieprz', 'szczypiorek']}),
#    ('Tuesday', {'name': 'tosty', 'ingredients': ['chleb', 'maslo', 'szynka']}),
#    ('Wednesday', {'name': 'kanapki', 'ingredients': ['bulki', 'margaryna', 'ser']}),
#    ('Thursday', {'name': 'owsianka', 'ingredients': ['banan', 'platki']}),
#    ('Friday', {'name': 'kawa', 'ingredients': ['ziarno', 'woda', 'mleko']})
#]

#for i in dishes_items:
#    print(f"day: {i[0]}, ingredients: {i[1]['ingredients']}")

for i in dishes_items:
    print(f"day: {i[0]}, ingredients: ", end="")
    for j in i[1]['ingredients']:
        print(j, end=", ")
    print()

#for day in dishes.keys():
#    print(f"day: {day} ingredients: {dishes[day]['ingredients']}")

# You have a list of foods, but you don’t know the order of the items (meaning that it can be: [“Strawberries”,
# “Potatoes”, “Karkóweczka”] or [“Potatoes”, “Karkóweczka”, “Strawberries”, “Sausage”]. Find your favourite food
# within the given list, print the food in a string. For example: “I love Karkóweczka”
print("Exercise 14")
foods = ["Potatoes", "Karkóweczka", "Strawberries", "Sausage"]

print("What's your favorite food?")
favorite = input()

for food in foods:
    if food == favorite:
        print(f"I love {food}")
