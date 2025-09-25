"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode:
get sales
if sales < 1000
    bonus = sales * 0.10
else:
    bonus = sales * 0.15
print bonus

get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 0.10
    else
        bonus = sales * 0.15
    print bonus
    get sales

print Program ended
"""

sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.10
else:
    bonus = sales * 0.15
print(f"Bonus is: ${bonus}")

"""
Test Case

Enter sales: $500
Bonus is: $50.0

Enter sales: $2000
Bonus is: $300.0

Enter sales: $1000
Bonus is: $150.0

"""

#Add loop
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(f"Bonus is: ${bonus}")
    sales = float(input("Enter sales: $"))

print("Program ended.")

"""
Test Case
Enter sales: $500
Bonus is: $50.0
Enter sales: $1000
Bonus is: $150.0
Enter sales: $2000
Bonus is: $300.0
Enter sales: $0
Bonus is: $0.0
Enter sales: $-1
Program ended.
"""