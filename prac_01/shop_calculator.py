"""
Program quickly work out the total price for a number of items, each with different prices.

Pseudocode:
total_price = 0
get number_of_items
while number_of_items < 0
    print Invalid number of items!
    get number_of_items

for i in range(number_of_items)
    get item_price
    total_price = total_price + item_price

if total_price > 100
    total_price = total_price * 0.9

print total price, items

"""
total_price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

# Discount
if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")

"""
Test Case

Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92

Number of items: 5
Price of item: 60
Price of item: 12.95
Price of item: 105.55
Price of item: 0.79
Price of item: 3
Total price for 5 items is $164.06
"""