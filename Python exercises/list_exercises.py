# create list with random number

import random

random_list = []
n = 5
for i in range(n):
    random_list.append(random.randint(0,50))
print(random_list)


# create list with random float number

random_float_list = []
n = 5
for i in range(n):
    random_float_list.append(random.random())
print(random_float_list)

# add item '1' to list [2, 4, 6]

list = [2, 4, 6]
print(list)

list.insert(0, 1)
print(list)

# write only even numbers from list [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_even = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_even)

for i in list_even:
    if (i % 2) == 0:
        print(i)

# remove element '5' from list [1, 2, 3, 4, 5]

remove_list = [1, 2, 3, 4, 5]
print(remove_list)
remove_list.remove(5)
print(remove_list)

# sum elements from list [1, 2, 3, 4]

sum_list = [1, 2, 3, 4]
print(sum_list)

suma = 0
for i in sum_list:
    suma = i + suma

print(suma)