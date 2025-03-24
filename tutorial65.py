# "Check if One String is a Substring of Another
# Problem: Given two strings s1 and s2, check if s2 is a substring of s1.
# Example:
# Input: s1 = ""hello world"", s2 = ""world""
# Output: True"

def search_substring(s,s1):
     return s1 in s           
str = input("Enter a string: ")
str1 = input("Enter substring: ")
print(search_substring(str,str1))
