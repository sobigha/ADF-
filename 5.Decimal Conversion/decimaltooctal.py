try:
    num=int(input())
    result=""
    while num!=0:
        rem=num%8
        num=num//8
        result=str(rem)+result
    print(result)
except:
    print("Exception")

#inbuilt function
print(oct(int(input())))
print(hex(int(input())))
print(bin(int(input())))