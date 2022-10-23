# # write calculator function
# # example
# # Write number A: 2
# # Write number B: 3
# # Sum: 5
# print("Write number A")
# numberA = input()
# print("Write number B")
# numberB = input()
#
# def suma(A, B):
#     return (int(A) + int(B))
#
# zmienna = suma(numberA, numberB)
# print(zmienna)
# print(suma(numberA, numberB))

# write function to calculate tip, price and tip % is provided by the user
# example
# Write price: 10.0
# Write tip%: 10
# Total price: 11.0 <--- price(10.0) + tip (1.0)

print("Write price")
price = input()
print("Write tip %")
user_tip = input()
tip_calculated = float(user_tip)/100

def total_price(price, tip):
    return float(price)+(float(price)*float(tip))

print(total_price(price,tip_calculated))


## write function to change celsius to fahrenheits

print("Write celsius")
celsius = input()

def changing (cel):
    return float(cel) * 1.8 + 32

print(changing(celsius))
