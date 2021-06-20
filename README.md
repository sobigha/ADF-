1.Program to read a file and store the unique words in a list sorted based on the length of word in a new file along with each word length appended to it.

import the re package.Initialiaze a set.Create a textfile and name it "text2.txt".Open the file and read contents from the file and store the contents in variable "file".Iterate each line.Replace the special characters with space using regex and split words by space.Then iterate the words,find the length and append it to the set.
Sort the set with respect to the length of the words and store in "l".Open a new file in write mode.Iterate the words and append it the newfile one by one.

2.Program to read a CSV (CSV with n number of columns) and store it in DICT of list.

import csv package.Create a csv file.Open that file and read the contents using csv.reader and store int "reader".Initialise a dictionary "result".Iterate the "reader" and store in key-value pair.Display the "result".

3.Program to Print all Prime Numbers in an Interval of 5 seconds

import time package.Intitialise a "start" to value 2.Start a inifinite loop by mentioning while True.
Initialise a "flag" variable to 0.Iterate by providing start range as 2 and end range as start//2+1.If start%i is divisible by 0,set the flag value to 1,break the loop else loop continues.After exiting the loop,check if flag is 0.If flag is 0, print the value.Then print the next value in next 5 seconds.Make the program sleep by Time.sleep(5).Increment start value by 1.Loop continues.

4.Program to Find HCF or GCD

Get the input from the user a and b.Check the condition if a is greater than b,if true assign b to "small" variable,if false assign a to "small" variable.Iterate the loop by providing start range as 1 and end range as small+1.If a is divisible by 0 and b is divisible by 0,set "gcd" to i value.After the loop terminates,check if a value is 0,if yes print the "b" value.Else if check b is 0,if yes print "a" value,else print the "gcd" value. 

5.Program to Convert Decimal to Binary, Octal and Hexadecimal

Decimal to Binary : 
Get the input from the user as "num".Initialse result.Check while num is not equal to 0.If true,store the remainder of num%2 in "rem".Store the quotient value in num by num//2.Append the result with rem.After Loop terminates,print result.

Decimal to octal : 
Get the input from the user as "num".Initialse result.Check while num is not equal to 0.If true,store the remainder of num%8 in "rem".Store the quotient value in num by num//8.Append the result with rem.After Loop terminates,print result.

Decimal to HexaDecimal :
Initialse list with values.Get the input from the user as "num".Initialise result.Check while num is greater than 0.If true,store the remainder of num%16 in "remainder".Append the result with list[remainder].Store the quotient in "num" by num//16.After loop terminates,print the result.

6.Program to Find ASCII Value of Character.

Get the input from the user.Using built-in function ord(),calculate the ascii value for the input and print the result.

7.Program to get an application (name , age , gender, salary, state, city)

Get the input from the user "name","gender","city","state" as string "age" as int and "salary" as float.Display the details.

