import sys
flag = 1
try:
    name=input("Enter Your Name :")
    age=int(input("Enter Your Age :"))

    while(flag):
        if(age>0):
          flag=0
        else:
          print("This is not valid age")
          age = int(input("ReEnter Your Age :"))

    flag=1
    gender=input("Gender :")
    x=gender.casefold()
    while (flag):
        if (x == "male" or x == "female"):
            flag = 0
        else:
            print("This is not valid gender")
            gender = input("ReEnter Gender :")
            x=gender.casefold()

    salary=float(input("Enter your Salary :"))
    city=input("Enter your City :")
    state=input("Enter your State :")

    print()
    print("Your Details ----")
    print("Name : ",name)
    print("Age : ",age)
    print("Gender : ",gender)
    print("Salary : ",salary)
    print("City : ",city)
    print("State : ",state)

except ValueError:
    print("Oops!  That was no valid input.  Try again...")

except:
    print("Unexpected error:", sys.exc_info()[0])
