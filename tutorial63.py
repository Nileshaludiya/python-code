# "Convert a String to an Integer
# Problem: Convert a numeric string into an integer without using int().
# Example:

# Input: ""1234""
# Output: 1234
# "

def convert_str_int(str1):
    print(type(str1))
    integer = int(str1)
    print(integer)
    print(type(integer))
str1 = input("Enter a string: ")
convert_str_int(str1)
