# "Count the Frequency of Each Character
# Problem: Given a string, count how often each character appears.
# Example:

# Input: ""apple""
# Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
# "

def count_letter(text):
    file = {}
    for x in text:
        if x in file:
            file[x] += 1
        else :
            file[x] = 1
    print(file)                
text = input("Enter a string: ")
count_letter(text)
