# "Find All Substrings of a String
# Problem: Given a string, print all possible substrings.
# Example:
# Input: ""abc""
# Output: ""a"", ""ab"", ""abc"", ""b"", ""bc"", ""c"""

def find_substring(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            print(s[i:j])
text = input("Enter a string: ")
find_substring(text)
