A = int(input("Enter value of A: "))
reversed = 0
for i in range(1,A+1):
    if( i % 2 == 0):
        reversed  += i
print("This is final answer: ",reversed)    
        