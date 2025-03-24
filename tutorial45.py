# "The parity of a number is even if it has an even number of 1s in its binary representation and odd otherwise.

# Write a function to find the parity of a number using division by 2.

# Example:
# Input: n = 9 (Binary: 1001, has 2 ones)
# Output: Even Parity"		

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
