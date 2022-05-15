def febonaci(a,b,c,r):
    d=b+c
    b=c
    c=d
    r.append(d) 
    if len(r)<=a:
        return febonaci(a,b,c,r)
    return r
        
a=int(input("Enter the number: "))
b,c=0,1
r=[0,1]
x=febonaci(a,b,c,r)
for i in range(len(x)):
    print(i, end=" ")
    
    
    
output

Enter the number: 
5
0 1 2 3 4 5 

** Process exited - Return Code: 0 **
Press Enter to exit terminal
