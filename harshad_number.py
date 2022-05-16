#   The sum of the digits of 21 is 3 i.e 2 + 1. As the number 21 is divisible by 3, It's a Harshad Number. is called harshad number


a=int(input("enter"))
c=a
sn=0
while a>0:
    b=a%10
    sn+=b
    a=a//10
    
if c%sn==0:
    print("it is harshad number")
else:
    print("no it is not harshan number")

    
    
    output
    
enter
21
it is harshad number


** Process exited - Return Code: 0 **
Press Enter to exit terminal
