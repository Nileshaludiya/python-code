money = int(input("Enter your money: "))
amount = int(input("debit (enter positive value) and credit (enter negative value) amount: "))
# if(money == 0 or amount == 0):
#     print("Your balance is 0")
if(amount > 0):
    sum = amount + money
    print("your amount after ADDITION = ",sum)
elif(amount < 0 ):
    if(money <  amount):
        print("Insufficient funds")
    else:
        sum = money + amount
    print("your amount after SUBTRACT",sum)

