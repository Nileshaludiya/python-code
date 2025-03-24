# "Write a function to count the number of 1s in a binary representation of a number using division by 2.

# Example:
# Input: n = 13 (Binary: 1101)
# Output: 3"		

def decimal_to_binary(num):
    binary_number = ""
    a = 0
    while num > 0:
        remainder = num % 2
        binary_number = str(remainder) + binary_number
        if remainder == 1:
            a = a + 1
        num = num // 2
    print("1 digit in binary number: ",a)
    return binary_number if binary_number else "0"     
num = int(input("Enter a value of the decimal: "))
print(decimal_to_binary(num))
