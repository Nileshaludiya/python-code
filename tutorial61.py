# """Count the Number of Vowels and Consonants
# Problem: Given a string, count the number of vowels and consonants in it.
# Example:
# Input: """"hello""""
# Output: Vowels: 2, Consonants: 3"""	

def check_vowel_consonant(text):
    vowel = "aeiouAEIOU"
    vow = 0
    con = 0
    for i in text:
        text.index(i)
        if i in vowel:
            # print("This is vowels: ",i)
            vow += 1
        else:
            # print("This is consonants: ",i)    
            con += 1
    print("vowels: ",vow)
    print("consonants: ",con)    
text = input("Enter a  string: ")
check_vowel_consonant(text)
 
