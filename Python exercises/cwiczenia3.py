#
# Create a file in your system (e.g. using notepad++ or vim). Given a file path, check if your name is present inside
# the file. Output file content line by line, but not the line where your name is. Feel free to use raw_input to get
# file path.
print("Exercise 14")

file = open("nowy 1.txt")
print(file.read())

name = "Karolina"

if file == name:
    print("Karolina is in the file")
else:
    print("Karolina is not in the file")

file.close()
#
# # Using loops and conditionals create a dictionary that contains month name and amount of days in that month for year
# # 2018.
print("Exercise 15")

year2018 = {
    "January": 0,
    "February": 0,
    "March": 0,
    "April": 0,
    "May": 0,
    "June": 0,
    "July": 0,
    "August": 0,
    "September": 0,
    "October": 0,
    "November": 0,
    "December": 0
}

monthNo = 1

for month in year2018:
    if month == "February":
        year2018[month] = 28
    elif monthNo in [1, 3, 5, 7, 8, 10, 12]:
        year2018[month] = 31
    else:
        year2018[month] = 30
    monthNo += 1

print(year2018)
#
# # Given list of dictionaries with following structure:
#
# # ●	change username to name and remove surname from “username”
# # ●	add new key “surname” and put the surname into that field
# # ●	print each employee without printing their id
#
print("Exercise 16")

myDictionary = [
    {
        "id": "123218736",
        "username": "John smith",
        "department": "IT",
    },
    {
        "Id": "83742638476",
        "username": "Kate White",
        "department": "Engineering"
    },
]

for i in range(0, len(myDictionary)):
    name = myDictionary[i]["username"].split(" ")[0]
    myDictionary[i]["name"] = name
    surname = myDictionary[i]["username"].split(" ")[1]
    myDictionary[i]["surname"] = surname
    del myDictionary[i]["username"]
    print(myDictionary[i].get("name") + " " + myDictionary[i].get("surname") + " " + myDictionary[i].get("department"))

# name = myDictionary[0]["username"].split(" ")[0]
# myDictionary[0]["name"] = name
# del myDictionary[0]["username"]
#
# name = myDictionary[1]["username"].split(" ")[0]
# myDictionary[1]["name"] = name
# del myDictionary[1]["username"]


# Create a “clock” that will print “Tick” each second for 1 minute. Output “5 seconds” each 5 “ticks”.
#
# Hints:

# 1 % 5 = 1
# 2 % 5 = 2
# 3 % 5 = 3
# 4 % 5 = 4
# 5 % 5 = 0
# 6 % 5 = 1
# 7 % 5 = 2
print("Exercise 17")
import time

current_time = time.time()

for i in range(1, 61):
    print("tic")
    if i % 5 == 0:
        print(str(i) + " seconds")
    time.sleep(1)

# Given you have a file with different sentences (you can use internet to get them, or just create your own one), for example:
#
# What a wonderful day! I’m very sleepy today. Are you looking for something? I’m so happy!
# Create a dictionary that categorizes the sentences by their emotions. For the example above:
# {
#      “questions”: [“Are you looking for something?”],
#      “exclamations”: [“What a wonderful day!”, “I’m so happy!”]
#      “neutral”: [“I’m very sleepy today”]
# }
print("Exercise 18")



dictionary = {
    "questions": [],
    "exclamations": [],
    "neutral": [],

}

file = open("sentences.txt")
lines = file.read().splitlines()

for line in lines:
    if line.find("!") >= 0:
        dictionary["exclamations"].append(line)
    elif line.find("?") >= 0:
        dictionary["questions"].append(line)
    else:
        dictionary["neutral"].append(line)

print(dictionary)

# Create a timer, that will print “ALARM!” when given amount of seconds have passed.
# Hints:
# import time
# # this will get current time in seconds since 1970:
# current_time = time.time()

print("Exercise 19")

import time

print("Enter seconds")
timer = int(input())
print(str(timer) + " seconds alarm clock")

time.sleep(timer)
print("ALARM!")

# Draw the following image using Python script :)
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#
# Hints: you can use 4 for loops for this task.


print("Exercise 19")

for i in range(5):
    print("*" * (i + 1))
for i in range(6):
    print("*" * (5 - i))



# You have 3 files that contain names and surnames. For example, a file can look like this:
#
# John Lennon | Senior Musician Architect
# James Bond | 007
#
#  Get an employee name through raw_input and print out:
# ●	Path to file that contains the employee name;
# ●	Each employee line from the file
# ●	The line that contains given employee name/surname should be printed in ** **. For example:
#             John Lennon | Senior Musician Architect
#             ** James Bond | 007 **
#
import os

print("Exercise 20")

print("Which employee do you need?")
worker = input()

files = ["employee1.txt", "employee2.txt", "employee3.txt"]

for fileName in files:
    file = open(fileName)
    file_content = file.read()

    if file_content.find(worker) >= 0:
        print(os.path.realpath(file.name))
        lines = file_content.splitlines()
        for line in lines:
            if line.find(worker) >= 0:
                print("** " + line + " **")
            else:
                print(line)


# employee1 = open("employee1.txt")
# employee1_content = employee1.read()
#
# if employee1_content.find(worker) >= 0:
#     print(os.path.realpath(employee1.name))
#     lines = employee1_content.splitlines()
#     for line in lines:
#         if line.find(worker) >= 0:
#             print("** " + line + " **")
#         else:
#             print(line)
#
# employee2 = open("employee2.txt")
# employee2_content = employee2.read()
#
# if employee2_content.find(worker) >= 0:
#     print(os.path.realpath(employee2.name))
#     lines = employee2_content.splitlines()
#     for line in lines:
#         if line.find(worker) >= 0:
#             print("** " + line + " **")
#         else:
#             print(line)
#
# employee3 = open("employee3.txt")
# employee3_content = employee3.read()
#
# if employee3_content.find(worker) >= 0:
#     print(os.path.realpath(employee3.name))
#     lines = employee3_content.splitlines()
#     for line in lines:
#         if line.find(worker) >= 0:
#             print("** " + line + " **")
#         else:
#             print(line)



#
#
# With variables (e.g. has_potatoes, has_water), if and else describe how you boil potatoes. Print out each step,
# for example: “Have no water. Getting water”, “Have potatoes, getting water.” Change variable values and execute
# python file several times to see if boiling process works correctly.
print("Exercise 21")

has_potatoes = True
has_water = False
has_pot = False

if has_potatoes == False:
    print("No potatoes, get potatoes")

print("Peel off potatoes")

if has_pot == False:
    print("No pot, get pot")

if has_water == False:
    print("No water, get water")

print("Put water into pot")
print("Boil water")
print("Put potatoes into the pot")
print("Boil 10 minutes")
print("Take out potatoes")

# With variables (has_fruits, has_milk), if and else describe how you make a milkshake. Print out each step,
# for example: “I have no milk. Getting milk”, “I have milk. Checking fruits.” Change variable values and execute
# python file several times to see if cooking process works correctly.

print("Exercise 22")

has_milk = False
has_banana = False
has_machine = True
has_chocolate = False

print("Get ingredients")
if has_milk == False:
    print("No milk, get milk")
else:
    print("Milk ready, check other ingredients")

if has_banana == False:
    print("No banana, get banana")
else:
    print("You have banana, look for chocolate")

if has_chocolate == False:
    print("No chocolate, get chocolate")
else:
    print("You have chocolate, continue")

if has_machine == False:
    print("No machine, prepare machine")
else:
    print("Everything is ready, put ingredients into machine")

print("Switch on the machine for 10 seconds")
print("Your milkshake is ready!")

# With variables (has_phone, has_phone_number)
# if and else describe how you make a call to a friend. Print out the steps, for example “My phone is dead. Need to
# recharge”. “Ublocking phone, checking if I have the number”. Change variable values and execute python file several
# times to see if cooking process works correctly.

print("Exercise 23")

has_phone = False
has_phone_number = False
is_phone_charged = False
is_phone_blocked = True
friend_can_talk = False

if has_phone == False:
    print("You have no phone, buy some phone")
else:
    print("You have a phone, let's call a friend")

if has_phone_number == False:
    print("No phone number, ask for phone number")
else:
    print("I'remember my friend's phone number, check if phone is charged")

if is_phone_charged == False:
    print("Phone is dead, recharge phone")
else:
    print("Phone is ready to use, check if it's unblocked")

if is_phone_blocked == False:
    print("Phone is blocked, unblock your phone")
else:
    print("Phone is unblocked, you can dial the number")

if friend_can_talk == False:
    print("Friend is not responding, call him later")
else:
    print("Hello my friend!")





