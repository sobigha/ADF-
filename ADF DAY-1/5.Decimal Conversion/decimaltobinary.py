import sys
result = ""
try:
    num = int(input())
    while num!=0:
        rem=num%2
        num=num//2
        result=str(rem)+result
    print(result)

except ZeroDivisionError as err:
    print('Handling run-time error:', err)

except ValueError:
    print("Oops!  That was no valid input.  Try again...")

except:
    print("Unexpected error:", sys.exc_info()[0])
