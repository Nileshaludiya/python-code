# "Count Even and Odd Digits in a Number
# Problem: Given a number N, count how many digits are even and how many are odd.
# Example:

# Input:  482351  
# Output: Even: 3, Odd: 3  "	



value = int(input("Enter a value: "))
A = len(str(value))
print("Total value: ",A)
a = 0
b = 0
for i in range(1,A+1):
    remainder = value % 10
    if(remainder % 2 == 0):
        a = len(str(remainder)) + a
    elif(remainder % 2 != 0):
        b = len(str(remainder)) + b
    value =  value // 10 
print("even value: ",a)
print("Odd value: ",b)       
        


# 34556767
# 5 = odd
# 3 = even        
         
