"""
CP1404/CP5632 - Practical
Make the appropriate choice of file-reading technique for each of these questions:

read()
readline()
readlines()
for line in file

"""
#1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
name = input("Enter your name: ")
out_file = open ("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2. write code that opens "name.txt" and reads the name (as above) then prints (note the exact output).
in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close
print(f"Hi {name}!")

#3.Create a text file called numbers.txt and save it in your prac directory. Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result.
