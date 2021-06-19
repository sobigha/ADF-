import time
start=2
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