def swapN(a,b):
    if(a<b):
        return b,a
n1=int(input("Enter number 1"))
n2=int(input("Enter number 2"))
print("Entered values are:")
print("Number 1:",n1,"Number 2:,n2")
print("Returned value from swap function:")
n1,n2=swapN(n1,n2)
print("Number1:",n1,"Number2:",n2)