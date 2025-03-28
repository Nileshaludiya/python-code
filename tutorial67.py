# "Find the First Non-Repeating Character
# Problem: Given a string, find the first character that does not repeat.
# Example:
# Input: ""aabbccdeff""
# Output: ""d"""

def first_non_repeating_letter(s):
    for i in s:
        if s.count(i) == 1:
            print(i)
            break
str1 = input("Enter a text: ")
first_non_repeating_letter(str1)
