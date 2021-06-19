import csv
f=open("read.csv","r")
reader=csv.reader(f)
result={}
for row in reader:
    result[row[0]]={'age':row[1],'dateofbirth':row[2]}

print(result)