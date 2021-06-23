
# inbuilt method
# print (math.gcd(num1,num2))
import sys

try:
    a = abs(int(input()))
    b = abs(int(input()))
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

except ZeroDivisionError as err:
   print('Handling run-time error:', err)

except ValueError:
  print("Oops!  That was no valid input.  Try again...")

except:
    print("Unexpected error:", sys.exc_info()[0])