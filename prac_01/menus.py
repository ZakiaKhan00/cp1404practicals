"""CP1404/CP5632 - Practical

Pseudocode:
get name
print menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       print "goodbye" name
   else
       print invalid message
   print menu
   get choice
print finished message
"""

MENU = ("(H)ello"
        "(G)oodbye"
        "(Q)uit")
name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")

    print(MENU)
    choice = input(">>> ").upper()

print("Finished.")

"""
Test Case
Enter name: Zakia
(H)ello(G)oodbye(Q)uit
>>> h
Hello Zakia
(H)ello(G)oodbye(Q)uit
>>> G
Goodbye Zakia
(H)ello(G)oodbye(Q)uit
>>> QUIT
Invalid choice
(H)ello(G)oodbye(Q)uit
>>> q
Finished.

"""