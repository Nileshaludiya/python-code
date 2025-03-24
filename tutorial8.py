a = int (input("enter your bill unit: "))
if(50>=a):
    print("amount :", a*0.50)
elif(  150>=a):
    print("amount :",((50*0.50)+(a-50)*0.75))
elif( 250>=a):
    print("amount :",((50*0.50)+(a-50)*0.75)(a-150*1.20))     
elif(250<a):
    print("amount :",((a-250)*1.50))       

