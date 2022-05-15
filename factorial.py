def factorial(a,sn):
    sn*=a
    if a>1:
        return factorial(a-1,sn)
    return sn
    
a=int(input("enter the number: "))
x=factorial(a,1)
print(x)



output


enter the number: 
7
5040


** Process exited - Return Code: 0 **
Press Enter to exit terminal
