# " Remove Duplicates from a String
# Problem: Given a string, remove duplicate characters while keeping the order.
# Example:

# Input: ""banana""
# Output: ""ban""
# "	

def remove_repeat_character(s):
    x = 0
    s1 = ""
    for i in s:
        if s.index(i) == x:
            s1 += i
        x += 1
    print(s1)        
text = input("Enter a string: ")
remove_repeat_character(text)
