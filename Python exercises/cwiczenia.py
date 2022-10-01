# 1. You have 2 pages in your application named login page and home page. You want to output page names.
print("Exercise 1")
page1 = "Login page"
page2 = "Home page"

page_names = page1 + " " + page2
print("Page names: "+page_names)

# 2. You have 2 pages in your application which are numbered. You want to output page numbers.
print("Exercise 2")
pagenr = "1", "2"
print("Page number: "+str(pagenr))


# 3. Find “You” word in string “Hello, world! You are awesome”. Print only the part after “You”.
# Result should look like this:
# >> ‘You are awesome’
print("Exercise 3")
text1 = "Hello, world! You are awesome"

find_you = text1.find("You")

print("'You' is located:" +str(find_you))

print(str("Hello, world! You are awesome"[find_you:]))


# 4. Create a variable that will greet you by your name. For example: “Good morning, Lucy!”. Make this string
# adjustable for different time of the day and different names. Output should look like this: >> Good morning,
# Bob! >> Good evening, Lucy!
print("Exercise 4")

import datetime
currentTime = datetime.datetime.now()

print("What's your name?")
name = input()

if currentTime.hour < 12 :
     print('Good morning ' + name + "!")
if currentTime.hour > 6 :
     print('Good evening ' + name + "!")


# 5. Create a greeting string with your name (e.g. “Hi, Lucy!”) and check if your name is actually inside of the string.

print("Exercise 5")
greeting = "Hi, Karolina!"
word_find = "Karolina" in "Hi, Karolina!"
print(word_find)

# 6. Make a calculation and output it’s result in the following format (number provided below is just an example):
# Result: 2384624
print("Exercise 6")
calculation = str(23425243+345345)
print("Result= "+ calculation)

# Make some calculations with big numbers (e.g. 12314141 and 138731623). Check that there is an 8 in the result.

print("Exercise 7")
multiplication = str(1231441*13244)
print("Result: "+ multiplication)
print("Search for a number...")
number = input()
number_find = number in multiplication
print("Number " + str(number) + " is in result: " + str(number_find))