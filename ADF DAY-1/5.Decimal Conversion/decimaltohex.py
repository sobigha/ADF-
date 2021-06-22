list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
num = int(input("Enter a number: "))
result = ''
try:
    while (num > 0):
        remainder = num % 16
        result = list1[remainder] + result
        num = num // 16
    print("Hexadecimal: ", result)
except:
    print("Exception")

    #solution:2
# num = int(input("Enter a number: "))
# result = ''
# out = ''
# try:
#     while (num > 0):
#         remainder = num % 16
#         if (remainder == 10):
#             out = 'A'
#         elif (remainder == 11):
#             out = 'B'
#         elif (remainder == 12):
#             out = 'C'
#         elif (remainder == 13):
#             out = 'D'
#         elif (remainder == 14):
#             out = 'E'
#         elif (remainder == 15):
#             out = 'F'
#         else:
#             out = str(remainder)
#         result = out + result
#         num = num // 16
#     print("Hexadecimal: ", result)
# except:
#     print("Exception")