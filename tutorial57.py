# Check if a String is a Palindrome
# Problem: Given a string, check if it reads the same forward and backward.
# Example:
# Input: "racecar"
# Output: True

def check_palindrome(s):
    a = s[::-1]
    if s == a :
        print("palindrome hai !!")
    else :
        print("palindrome nhi hai!!")   
str1 = input("Enter a string: ")
check_palindrome(str1)
