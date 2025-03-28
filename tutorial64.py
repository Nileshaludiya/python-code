def find_substring(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            print(s[i:j])
text = input("Enter a string: ")
find_substring(text)