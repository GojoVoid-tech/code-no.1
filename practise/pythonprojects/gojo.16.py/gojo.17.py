def convertToTitle(string):
    titleString=string.title();
    print("The input string in the title case is:",titleString)
userinput=input("Write the sentence:")
totalSpace=0
for b in userinput:
    if b.isspace():
        totalSpace+=1
if(userinput.istitle()):
    print("The String is already in title case")
elif(totalSpace>0):
    convertToTitle(userinput)
else:
    print("The String is of one word only")