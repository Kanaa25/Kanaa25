# create dictionary with elements 'One' = 1, 'Two' = 2, 'Three' = 3

element_dict = {
    "One": 1,
    "Two": 2,
    "Three": 3
}
print(element_dict)

# print dictionary keys
# { "One": 1, "Two": 2, "Three": 3}

print(element_dict.keys())
for i in element_dict:
    print(i)
# print dictionary values
# { "One": 1, "Two": 2, "Three": 3}

for i in element_dict:
    print(element_dict[i])


# add value "four" = 4 to dictionary
# { "One": 1, "Two": 2, "Three": 3}

element_dict["Four"] = 4
print(element_dict)

# remove value "One" from dictionary
# { "One": 1, "Two": 2, "Three": 3}

element_dict.pop("One")
print(element_dict)

# change dictionary items from
# { "One": { value: 1 }, "Two": { value: 2 }, "Three": {value: 3 }}
# to (add isEven)
# { "One": { value: 1, isEven: false }, "Two": { value: 2, isEven: true }, "Three": {value: 3, isEven: false }}

new_dict = {
    "One": {
        "value": 1
    },
    "Two": {
        "value": 2
    },
    "Three": {
        "value": 3
    }
}

for number in new_dict:
    if new_dict[number]["value"] % 2 == 0:
        new_dict[number]["isEven"] = True
    else:
        new_dict[number]["isEven"] = False
print(new_dict)