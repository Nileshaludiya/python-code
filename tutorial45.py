def decimal_to_binary(num):
    binary_number = ""
    a = 0
    while num > 0:
        remainder = num % 2
        binary_number = str(remainder) + binary_number
        if remainder == 1:
            a = a + 1
        num = num // 2
        # print(num,"num")
    print("1 digit in binary number: ",a)
    if(a % 2 == 0):
        print("This num is Even parity")
    else:
        print("This num is non Even parity")
    return binary_number if binary_number else "0"     
num = int(input("Enter a value of the decimal: "))
print(decimal_to_binary(num))