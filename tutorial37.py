# "Write a program to print the multiplication table of the number entered by the user, N.

# The table for input N = 5 should get displayed in the following form:"	

def table_number(N):
    for i in range(1,11):
        mul = N*i
        print(N ,"X",i ,"=", mul)
N = int(input("Enter a value that requires table: "))
table_number(N)
