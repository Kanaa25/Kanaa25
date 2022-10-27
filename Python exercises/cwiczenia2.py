# Create a dictionary that describes a person's contact information. Print name and phone number as one string with explanation. For example:
# “Bob Dylan, phone number: 000-000-000”

print("Exercise 8")

dictionary1 = {
    'Name': 'Tomasz Nowak',
    'Phone number': "111 - 222 - 333"
}
dictionary2 = {
    'Name': 'Piotr Kowalski',
    'Phone number': "123 - 123 - 123"
}

print(f"First: {dictionary1.get('Name')} phone number: {dictionary1.get('Phone number')}" '\n'
      f"Second: {dictionary2.get('Name')} phone number: {dictionary2.get('Phone number')}")

# Create a list of  dictionaries that describe a worker (his name/surname, position, project etc). Print one of the worker’s information.
# There is a string that describes employee information, e.g.:
# “Lilly;Brown;QA Engineer;Samsung”
# List values are separated with “;”.
# Print out a string that represents name, surname, position and project from the given string with explanation. For example:
# Name: Lilly, Surname: Brown. Position: QA Engineer, project: Samsung.
# Note: you can use list indexes to form the output string.

print("Exercise 9")

first = {
    'Name': "Lilly",
    'Surname': "Brown",
    'Position': "QA Engineer",
    'Project': "Samsung"
}

print(f"Position: {first.get('Position')}")

print("Name:" + str(first.get("Name")), "Surname:" + str(first.get("Surname")),
      "Position:" + str(first.get("Position")), "Project:" + str(first.get("Project")))

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

carList = {
    "Ford Fiesta": {
        "year": 2014,
        "color": "Candy blue"
    },
    "Seat Leon": {
        "year": 2018,
        "color": "Desire red"
    }
}

print("You picked `" + list(carList.keys())[1] + "`. Selected color: " + carList.get("Seat Leon").get("color") +
      ", year of production: " + str(carList.get("Seat Leon").get("year")))

# Create a dictionary that describes your laptop technical details (e.g. RAM, hard drive capacity etc.) Using the
# get() method of dictionaries print out existing and missing information. You should use get() at least once for
# each case: get(existing key) get(missing key) get(missing key, default value)

print("Exercise 11")

myLaptop = {
    "Name": "Asus",
    "RAM": "8 GB",
    "Hard drive": "1 TB",
}
myLaptop.setdefault("Size", "Default size 1")

print("My laptop name: " + str(myLaptop.get("Name")) + ". My laptop RAM: " + str(myLaptop.get("RAM")) + ". My laptop "
                                                                                                        "weight: " + str(
    myLaptop.get("weight")) + ". My laptop size: " + str(myLaptop.get("Size")))

# You have a string: “My name is Bob”. Using [:], split() and append() methods, create a string that replaces Bob with your name.
print("Exercise 12")

originalText = "My name is Bob"
print(originalText.split())

changedText = (originalText.split())
changedText.append("Karolina")

print(changedText[0], changedText[1], changedText[2], changedText[4])

# Think about 7 favourite dishes that you like. Now, you have to create a schedule of eating them each day. Create a
# dictionary with 7 keys (names of week days). For each key the value will be a dictionary containing the name of
# your favourite dish and list of ingredients that you have to buy to cook it.
print("Exercise 13")
# Try to print out ingredients for different days of the week.

dishes = {
    "Monday": {
        "name": "jajecznica",
        "ingredients": ["jajko", "sol", "pieprz", "szczypiorek"]
    },
    "Tuesday": {
        "name": "tosty",
        "ingredients": ["chleb", "maslo", "szynka"]
    },
    "Wednesday": {
        "name": "kanapki",
        "ingredients": ["bulki", "margaryna", "ser"]
    },
    "Thursday": {
        "name": "owsianka",
        "ingredients": ["banan", "platki"]
    },
    "Friday": {
        "name": "kawa",
        "ingredients": ["ziarno", "woda", "mleko"]
    },
}

for day in dishes:
    print("day: " + day + " ingredients: " + str(dishes.get(day).get("ingredients")))

# You have a list of foods, but you don’t know the order of the items (meaning that it can be: [“Strawberries”,
# “Potatoes”, “Karkóweczka”] or [“Potatoes”, “Karkóweczka”, “Strawberries”, “Sausage”]. Find your favourite food
# within the given list, print the food in a string. For example: “I love Karkóweczka”
print("Exercise 13")
foods = ["Potatoes", "Karkóweczka", "Strawberries", "Sausage"]

print("What's your favorite food?")
favorite = input()

for food in foods:
    if food == favorite:
        print("I love " + food)
