"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data from file and display subject details."""
    subjects = load_data(FILENAME)
    display_subjects(subjects)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    input_file.close()

    return subjects

def display_subjects(subjects):
    """Display subject details"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students.")


main()

"""
Test Case:
CP1401 is taught by Ada Lovelace and has 192 students.
CP1404 is taught by Alan Turing  and has  98 students.
CP4321 is taught by Bill Gates   and has 676 students.
CP1234 is taught by Steve Jobs   and has 123 students.
"""