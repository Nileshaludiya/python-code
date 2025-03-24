def table_number(N):
    for i in range(1,11):
        mul = N*i
        print(N ,"X",i ,"=", mul)
N = int(input("Enter a value that requires table: "))
table_number(N)