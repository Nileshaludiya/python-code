# Problem Description
# Write a program to input three numbers(A, B & C) from user and print the maximum element among A, B & C in each line.
# Problem Constraints
# 1 <= A <= 1000000
# 1 <= B <= 1000000
# 1 <= C <= 1000000


# Input Format
# First line is a single integer A.
# Second line is a single integer B.
# Third line is a single integer C.


# Output Format
# One line containing an integer as per the question.

# Example Input
# Input 1:
# 5
# 6
# 7
# Input 2:
# 1000
# 10000
# 100000

# Example Output
# Output 1:
# 7
# Output 2:
# 100000

a = float(input("Enter first number :"))
b = int(input("Enter second number :"))
c = float(input("Enter third number :"))
if(a>=b and a>=c):
    print("greatest number a",a)
elif(b>=c):
    print("greatest number b :",b)
else:
    print("greatest number c :",c)    
