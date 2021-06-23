import sys
try:
    num = int(input())
    result = ""
    while num!=0:
        rem=num%8
        num=num//8
        result=str(rem)+result
    print(result)

except ZeroDivisionError as err:
   print('Handling run-time error:', err)

except ValueError:
    print("Oops!  That was no valid input.  Try again...")

except:
    print("Unexpected error:", sys.exc_info()[0])


#inbuilt function
    print(oct(int(input())))
    print(hex(int(input())))
    print(bin(int(input())))