
'''
frendly number=The numbers whose ( sum of divisors ) / number ratio is same are known as Friendly Pair Numbers.
                Let's try and understand it better using an example

Example
Input : 6 28
Output : Yes, they are a friendly pair
Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
Now the sum of factors of both the numbers are 6 and 28 respectively. 
When we divide the sums with the numbers we get 1 and 1 respectively. 
As the ratio of both the number match, they are considered as a friendly pair.
'''



a=int(input("enter"))
b=int(input("enter"))
def frendly(a):
    b=a
    sn=0
    a//=2
    for i in range(1,a+1):
        if b%i==0:
            sn+=i
            
    return b//sn
    
c=frendly(a)
d=frendly(b)
if c==d:
    print("yes")
else:
    print("no")
    
    
    output
    

    enter
6
enter
28
yes


** Process exited - Return Code: 0 **
Press Enter to exit terminal
