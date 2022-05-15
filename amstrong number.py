def amst_range(a,b):
    w=[]
    for i in range(a,b):
        sm=0
        d=i
        while i>0:
            c=i%10
            sm+=c**len(str(d))
            i//=10
            
        if sm==d:
            w.append(d)
        
    return w
    
a=int(input("enter the nummber: "))
b=int(input("enter the number: "))
d=amst_range(a,b)
print(d)





output


enter the nummber: 
150
enter the number: 
160
[153]


** Process exited - Return Code: 0 **
Press Enter to exit terminal
