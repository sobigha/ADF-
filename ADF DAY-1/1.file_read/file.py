import re
import sys
res=set({})
try:
    filename=input("Enter the filename")
    file=open(filename,"r")
    Lines = file.readlines()
    for line in Lines:
        string = re.sub("[^0-9a-zA-Z]", " ",line).split(" ")

        for s in string:
           if(s!=""):
              p=len(s)
              res.add(str(p)+s)

    l = list(sorted(list(res), key=len))
    with open('newfile.txt', 'w+') as f:
        for items in l:
            f.write('%s ' % items)
        print("File written")
    f.close()

except IOError:
   print ("Error: can\'t find file or read data")
# except ValueError:
#   print("Oops!  That was no valid input.  Try again...")
except:
    print("Unexpected error:", sys.exc_info()[0])