def search_substring(s,s1):
     return s1 in s           
str = input("Enter a string: ")
str1 = input("Enter substring: ")
print(search_substring(str,str1))