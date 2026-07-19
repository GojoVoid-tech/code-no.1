userinput=input("Write a sentence:")
totalChar=len(userinput)
print("Total Characters:",totalChar)
totalAlpha=totalDigit=totalSpecial=0
for a in userinput:
    if a.isalpha():
        totalAlpha+=1
    elif a.isdigit():
        totalDigit+=1
    else:
        totalSpecial+=1
print("Total Alphabets:",totalAlpha)
print("Total Digits:",totalDigit)
print("Total Special Characters:",totalSpecial)
totalSpace=0
for b in userinput:
    if b.isspace():
        totalSpace+=1
print("Total Words in the input:",(totalSpace+1))