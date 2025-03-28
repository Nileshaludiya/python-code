def first_non_repeating_letter(s):
    for i in s:
        if s.count(i) == 1:
            print(i)
            break
str1 = input("Enter a text: ")
first_non_repeating_letter(str1)