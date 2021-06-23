import time
import sys

start=2
try:
    while True:
            flag = 0
            for i in range(2, start//2+1):
                if (start % i) == 0:
                    flag=1
                    break
            if(flag==0):
                print(start)
                time.sleep(5)
            start=start+1

except ZeroDivisionError as err:
   print('Handling run-time error:', err)
except ValueError:
  print("Oops!  That was no valid input.  Try again...")
except:
    print("Unexpected error:", sys.exc_info()[0])