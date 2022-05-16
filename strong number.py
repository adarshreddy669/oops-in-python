# strong number is a number if it is like
# sum of factorial of the given number is == the number itself

def strong(a,sn):
    c=a%10
    f=1
    for i in range(1,c+1):
        f*=i
        
    sn+=f
    a=a//10
    if a>0:
        return strong(a,sn)
        
    return sn
    
   
a=int(input("Enter the number: "))
b=a
k=strong(a,0)
if k==b:
    print("Yes, no is strong")
else:
    print("no, nm is not strong")
        

      
      
output

Enter the number: 
145
Yes, no is strong


** Process exited - Return Code: 0 **
Press Enter to exit terminal
