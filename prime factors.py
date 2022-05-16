def factors(a):
   
    d=""
    for i in range(2,(a//2)+1):
        if a%i==0:
            flag=0
            c = i**(1/2)
            c=int(c)
            for j in range(2,c+1):
                if i%j==0:
                    flag=1
                
            if flag==0:
                d+=str(i)+" "
                    
    return d
  
a=int(input("Enter the input: "))  
n=factors(a)
print(n)



output

Enter the input: 50
  2 5

Session Killed due to Timeout.
Press Enter to exit terminal
