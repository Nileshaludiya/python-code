def divisiblenumber(num):
    if(num%5==0):
        if(num%11==0):
            print("This number is divisible by 5 or 11")
        else:
            print("This number is divisible by only 5")    
    elif(num%11==0):
        print("This number is divisible by only 11")
    else:
        print("this num is not divisible by 5 or 11")

num = int(input("enter a number: "))
divisiblenumber(num)