'''
A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.
Let's try and understand the concept better using an example

Example
Input : Number = 12
Output : Yes, It's an Abundant Number
Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
Now the sum of the factors except the number itself is :
1 + 2 + 3 + 4 + 6 = 16
as the number 16>12 , the number itself.
It's an abundant number.
'''



a=int(input("enter"))
c=a
a=a//2
sn=0
while a>0:
    if c%a==0:
        sn+=a
    a-=1
    

    
if c<sn:
    print("it is abundant number")
else:
    print("no it is not abundent number")


 output
 
 enter
12
it is abundant number


** Process exited - Return Code: 0 **
Press Enter to exit terminal
