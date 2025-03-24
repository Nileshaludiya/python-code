# You are given an integer A, you need to find and return	
	
# the sum of all the even numbers between 1and A.	
# Even numbers are those numbers that are divisible by 2.	
    
A = int(input("Enter value of A: "))
reversed = 0
for i in range(1,A+1):
    if( i % 2 == 0):
        reversed  += i
print("This is final answer: ",reversed)    
        
