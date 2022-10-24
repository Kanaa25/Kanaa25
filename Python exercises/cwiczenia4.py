# # Given a random list of numbers, pass it to a function and return:
# # ●	“Float” if number is a float
# # ●	“Int” if number is int
# # ●	None if number is a 0
# #
# # Do the loop outside of the function. Try using list comprehension for this task.
print("Exercise 24")

import random

rand_list = []
n = 1
for i in range(n):
    rand_list.append(random.random())
print(rand_list)


def variable_type(rand_list):
    if rand_list == 0:
        print("None")
    elif type(rand_list[0]) is int:
        print("Int")
    elif type(rand_list[0]) is float:
        print("Float")


variable_type(rand_list)

# Given you have a dictionary with the following structure (or data.json file) containing:
# {
#     “Samsung Galaxy S 9”: {
#         “Year”: 2018
#     },
#     “Samsung Galaxy Young”: {
# #         “Year”: 2011
# #     }
# # }
# #
# # Write a function that checks which year the phone was constructed. Return “review technical state” if phone is
# # older than year 2016. Update the dictionary for each phone model with “action”:  <response from the function> if
# # action is needed.
#
print("Exercise 25")

phone_Dictionary = {
    "Samsung Galaxy S 9": {
        "Year": 2018
    },
    "Samsung Galaxy Young": {
        "Year": 2011
    }
}


def construction_year(phone):
    if phone['Year'] < 2016:
        return "Review technical state"
    else:
        return "Phone is ok"


for phone_Name in phone_Dictionary:
    if construction_year(phone_Dictionary[phone_Name]) == "Review technical state":
        phone_Dictionary[phone_Name]['Action'] = "Review technical state"

print(phone_Dictionary)

#
# Write a function that accepts a year as parameter and prints if it’s a leap year or not. Input of the year should
# come from the input().
#
# Feel free to use infinite loop in this example, but remember to have a user interface to stop your program.
#
# Example of interaction:
# Please, enter year: 2018
# Not leap year
#
# Please, enter year: 2012
# Leap year
#
# Stop
# <program ends>

print("Exercise 26")

print("Please, enter year:")
given_year = int(input())

def checkLeap(year):
    if ((year % 400 == 0) or (year % 100 == 0) and (year % 4 ==0)):
        return("{0} is a leap year".format(year))
    else:
        return("{0} is not a leap year".format(year))

print(checkLeap(given_year))


# Write a function that accepts a month name as parameter and prints if month has 30 or 31 or 28/29 days. Input of
# the month name should come from input().
#
# Feel free to use infinite loop in this example, but remember to have a user interface to stop your program.
#
# Example:
# Please, enter month: July
# 31 days
# Please, enter month: June
# 30 days
# Stop
# <program ends>

#
print("Exercise 27")

print("Please, enter month:")
my_month = input()

def days(month):
    if month == "February":
        return("No. of days: 28/29 days")
    elif month in ("April", "June", "September", "November"):
        return("No. of days: 30 days")
    elif month in ("January", "March", "May", "July", "August", "October", "December"):
        return("No. of days: 31 day")
    else:
        return("Wrong month name")

print(days(my_month))

#
# Write a function that accepts time input and replies in other format. For example:
# >>> Please, enter time:
# 14:30
# >>> 2:30 PM
# >>> Please, enter time:
# 2:50 AM
# >>> 2:50
#
# Feel free to use infinite loop in this example, but remember to have a user interface to stop your program.
#
# Input of time should come from input().
print("Exercise 28")
import time

print("Exercise 27")
print("Please, enter time: ")
my_time_str = input()


def timechange(t , format) :
    return (time.strftime(format , t))


if my_time_str.endswith("pm") or my_time_str.endswith("am") :
    my_time = time.strptime(my_time_str , "%I:%M %p")
    print(timechange(my_time , "%H:%M"))
else :
    my_time = time.strptime(my_time_str , "%H:%M")
    print(timechange(my_time , "%I:%M %p"))

# Write a function that multiplies any number of given numbers and returns a result. E.g.:
# >>> multiply(2, 2, 3)
# 12
# >>> multiply(0, 1)
# 0
# ...

print("Exercise 29")
import math

print("Please, enter your numbers: ")
my_numbers = input()
number_list = my_numbers.split()
print(number_list)
number_list = [int(i) for i in number_list]


def multiply(numbers):
    total = math.prod(numbers)
    return total


print(multiply(number_list))

# Given a file with text, verify that each line does not contain numbers and  “&”, “?”, “/” signs. For each
# verification create a separate function that returns if verification passed. Your application may accept file path
# from console. Please, output verification results in a human readable format (for example: “Verification failed!
# Please, remove ? signs” or “Verification passed”).

print("Exercise 30")

file = open("sentences.txt", "r")
lines = file.read().splitlines()

sign1 = "&"
sign2 = "?"
sign3 = "/"


def filereading(file):
    for line in lines:
        if line.find(sign1) >= 0:
            return ("Verification failed. Please, remove & sign.")
        elif line.find(sign2) >= 0:
            return("Verification failed. Please, remove ? sign.")
        elif line.find(sign3) >= 0:
             return("Verification failed. Please, remove / sign.")
        else:
             return("Verification passed")

print(filereading(file))
