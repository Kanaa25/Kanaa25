# # write all even numbers from 1 to n (n is provided by the user), use loops
# print("Write your number")
# number = input()
#
# for i in range(1,int(number)):
#     if (i % 2) == 0:
#         print(i)
#
# # write "yes" if value provided by the user contains letter "a", otherwise "no"
# print("Write your text")
# text = input()
#
# if text.find("a") >= 0:
#     print("Yes")
# else:
#     print("No")

# write currency sign for value provided by the user (options are "PLN", "USD", "EUR")
# PLN -> ZL
# USD -> $
# EUR -> E
# JPN -> J
# other -> unknown

while True:

    print("Write the price")
    price = input()

    if price.find("PLN") >= 0:
        print("ZL")
    elif price.find("USD") >= 0:
        print("$")
    elif price.find("EUR") >= 0:
        print("E")
    elif price.find("JPN") >= 0:
        print("J")
    else:
        print("Unknown")



