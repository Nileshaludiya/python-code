def count_letter(text):
    file = {}
    for x in text:
        if x in file:
            file[x] += 1
        else :
            file[x] = 1
    print(file)                
text = input("Enter a string: ")
count_letter(text)