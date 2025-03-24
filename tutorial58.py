# "Capitalize the First Letter of Each Word
# Problem: Given a sentence, capitalize the first letter of each word.
# Example:

# Input: ""hello world""
# Output: ""Hello World"""	

def first_letter_capital(text):
    return text.title()

text = input("Enter a string: ")
print(first_letter_capital(text))
