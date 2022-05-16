# perfect number is the number 
# (sum of the factors of the number == the number itself) is called perfect number




def perfect_number(a,sn,i):
    if a%i==0:
        sn+=i
        
    if i>1:
        return perfect_number(a,sn,i-1)
    return sn
    
a=int(input("Enter the number: "))
k=perfect_number(a,0,a//2)
if k==a:
    print("yes it is perfect number")
else:
    print("no, it is not a perfect number")
    
    
    
    output
    
 Enter the number: 
28
yes it is perfect number


** Process exited - Return Code: 0 **
Press Enter to exit terminal
