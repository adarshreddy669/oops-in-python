# automorphic number = last digit of the number and squared number should be equal


def automorphic(a):
    return a**2
    
a=int(input("Enter the numebr: "))
k=automorphic(a)
b,a=k%10,a%10
if a==b:
    print("yes, no is a automorphic number")
    
else:
    print("no, no is not automorphic")

    
    output
    
Enter the numebr: 
890625
yes, no is a automorphic number


** Process exited - Return Code: 0 **
Press Enter to exit terminal
