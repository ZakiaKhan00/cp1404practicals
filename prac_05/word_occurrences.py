"""
CP1404/CP5632 Practical
Word Occurrences

Estimate: 15 minutes
Actual:  23 minutes
"""

#count the occurrences
word_counts = {}
text = input("Text: ").lower().split()

for word in text:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

# Find the length of the longest word
max_length = max(len(word) for word in word_counts)

# Print counts nicely
for word in sorted(word_counts):
    print(f"{word:{max_length}} : {word_counts[word]}")




