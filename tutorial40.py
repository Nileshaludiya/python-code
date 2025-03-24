
# Remove a Specific Digit from a Number
# Problem: Given a number N and a digit D, remove all occurrences of D from N.
# Example:

# Input:  N = 10501, D = 0  
# Output: 151  

N = int(input("Enter a value of N: "))
D = int(input("Enter the value you want to remove: "))
B = " "
A = len(str(N))
# print("length of value",A)
for i in range(1,A+1):
    remainder = N % 10
    if(remainder != D):
        B += str(remainder)          
    N = N // 10
# print("After remove digit: ",B)
str1 = ""
b = int(B)
C = len(str(b))
for j in range(1,C+1):    
    rem = b % 10
    b = b // 10
    str1 += str(rem)
print("conform digit: ",str1)
