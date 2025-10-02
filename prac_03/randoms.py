import random

print(random.randint(5, 20))  # line 1
#Each time I run Line 1, it prints a random number between 5 and 20 inclusively.
#Smallest: 5
#Largest: 20

print(random.randrange(3, 10, 2))  # line 2
#Each time I run Line 2, it prints a random number either 3,5,7,9
#Smallest: 3
#Largest: 9
#Could it produce 4? No, 4 doesn't fall in that sequence

print(random.uniform(2.5, 5.5))  # line 3
#Each time I run Line 3, it prints floating numbers between 2.5 and 5.5
#Smallest: 2.5
#Largest: 5.5

print(random.randint(1,100))