def reversed_string(str1):
    length = len(str1)
    # print(length)
    for i in range(length-1,-1,-1):
        print(str1[i],end="")
str1 = input("Enter a string: ")
reversed_string(str1)