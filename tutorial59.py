# Find the Longest Word in a Sentence
# Problem: Given a sentence, find the longest word.
# Example:

# Input: "I love programming"
# Output: "programming"

def longest_world(text):
    list1 = text.split()
    
    return max(list1)
text = input("Enter a string: ")
print(longest_world(text))
