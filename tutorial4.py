marks = int (input("Enter your marks :"))

if(marks >= 90):
    grate = "A"
elif(marks < 90 and marks >= 80):
    grate = "B"
elif(marks < 80 and marks >= 70):
    grate = "C"
else:
    grate = "D"
print("The grate of student :",grate)       