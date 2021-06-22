num=int(input())
result = ""
try:
    while num!=0:
        rem=num%2
        num=num//2
        result=str(rem)+result
    print(result)
except:
    print("Exception")

