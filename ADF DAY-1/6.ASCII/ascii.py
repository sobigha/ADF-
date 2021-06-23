import sys
try:
    c = input()
    print("The ASCII value of '" + c + "' is", ord(c))

except ValueError:
  print("Oops!  That was no valid input.  Try again...")

except:
    print("Unexpected error:", sys.exc_info()[0])

