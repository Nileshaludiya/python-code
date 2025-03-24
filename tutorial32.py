Given an integer N, print the corresponding pattern for N.
A
A B
A B C
A B C D

for i in range(1 , 5):
    A = 65
    for i in range(1 , i+1):
        print( chr(A) ,end = " ")
        A = A + 1

    print()    
