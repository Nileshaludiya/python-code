def check_palindrome(s):
    a = s[::-1]
    if s == a :
        print("palindrome hai !!")
    else :
        print("palindrome nhi hai!!")   
str1 = input("Enter a string: ")
check_palindrome(str1)