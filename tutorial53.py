def con_binary_to_decimal(num):
    decimal_number = 0
    i = 0
    while num > 0:
        remainder = num % 10
        decimal_number += remainder * 2**i
        num //= 10
        i += 1
    return decimal_number    
num = int(input("Enter a number from 0 and 1: "))
print(con_binary_to_decimal(num))