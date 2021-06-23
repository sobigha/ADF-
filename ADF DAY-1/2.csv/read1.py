import csv
import sys
try:
    filename = input("Enter the filename")
    file = open(filename, "r")
    reader=csv.reader(file)
    result={}
    for row in reader:
        result[row[0]]={'age':row[1],'dateofbirth':row[2]}

    print(result)

except IOError:
   print ("Error: can\'t find file or read data")
# except ValueError:
#   print("Oops!  That was no valid input.  Try again...")
except:
    print("Unexpected error:", sys.exc_info()[0])