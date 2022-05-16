def power(a,b,sn,i):  #using recursion
    sn*=a
    i+=1
    if i<=b:
        return power(a,b,sn,i)
        
    return sn

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=power(a,b,1,1)
print(c)


output

Enter the number: 
4
Enter the number: 
2
16


** Process exited - Return Code: 0 **
Press Enter to exit terminal



# using operator

def power(a,b):
    return a**b

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=power(a,b)
print(c)
