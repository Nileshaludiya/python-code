n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if(n1 < n2):
    if(n1 < n3):
        print("minimum number is ",n1)
    else:
        print("minimum number is ",n3)
else:
    if(n2 < n3):
        print("minimum number is ",n2)  
    else:
        print("minimum number is ",n3)              