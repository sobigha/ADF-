import re

res=set({})
file=open("text2.txt","r")
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