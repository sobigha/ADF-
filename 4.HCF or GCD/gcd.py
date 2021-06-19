
# inbuilt method
# print (math.gcd(num1,num2))

a=abs(int(input()))
b=abs(int(input()))
try:
    if(a>b):
        small=b
    else:
        small=a

    for i in range(1,small+1):
         if((a%i==0) and (b%i==0)):
             gcd=i

    if(a==0):
        print(b)
    elif(b==0):
        print(a)
    else:
       print(gcd)
except:
    print("Exception")