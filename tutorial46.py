def con_to_binary(num):
    binary_number = ""
    while num > 0:
        remainder = num % 2
        binary_number = str(remainder) + binary_number
        num = num // 2    
    b = str(binary_number)
    print("After reversing",*reversed(b)) 
    return binary_number if binary_number else "0"    
num = int(input("Enter a value: "))
print(con_to_binary(num),"before reversing")
