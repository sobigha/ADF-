import sys
import re

try:
    file = input("Enter the filename: ")
    list=open(file, 'r')
    list1=[]
    string=""
    for line in list:
         string = re.sub("[^0-9a-zA-Z]", " ",line).split(" ")
         for word in string:
             if(word!=""):
               list1.append(word)

    count_prefix=0
    count_suffix=0
    maximum_word=""
    palindrome_word=[]
    vowels_split=""
    capitalize_3rdletter=""
    capital_5thword=""
    hyphen_split=""
    semicolon_replace=""

    def prefix():
        result=[]
        global count_prefix
        for word in list1:
            if word.startswith("to"):
                result.append(word)
                count_prefix=count_prefix+1
       # print(count_prefix)
       # file()

    def suffix():
        result = []
        global count_suffix
        for word in list1:
            if word.endswith("ing"):
                result.append(word)
                count_suffix=count_suffix+1
        #print(count_suffix)
        #file()

    def maximumword():
        counter=0
        global maximum_word
        for i in list1:
            curr_frequency = list1.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                maximum_word = i
       # print(maximum_word)
        #file()

    def palindrome():
        global palindrome_word
        for i in list1:
            if(i == i[::-1]):
                palindrome_word.append(i)
        #print(palindrome_word)
        #file()

    def uniqueList():
        unique=[]
        for x in list1:
            if x not in unique:
                unique.append(x)
        print(unique)

    def dictWord():
        dict_word=[]
        for element in enumerate(list1):
           dict_word.append(element)
        print(dict_word)


    def vowels():
        global vowels_split
        vowels_split= [re.sub("[aeiouAEIOU]", ' ', i) for i in list1]
        # for i in vowels_split:
        #     print(i, end=" ")
       # print()
        #file()

    def capitalize_thirdletter():
        global capitalize_3rdletter
        list = open("text1.txt", 'r')
        for line in list:
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                if (s != ""):
                    result = ""
                    for i in range(1, len(s) + 1):
                        if i == 3:
                            result += s[i - 1].upper()
                        else:
                            result += s[i - 1]
                    capitalize_3rdletter+=result+' '

       # print(capitalize_3rdletter)
      #  print()


    def capitalize_5thword():
        global capital_5thword

        for i in range(1, len(list1)):
            result = ""
            if (i % 5 == 0):
                result += list1[i].upper()
            else:
                result += list1[i]
            capital_5thword+=result+" "
        #print(capital_5thword)

    def hypen():
        global hyphen_split
        list = open("text1.txt", 'r')
        hyphen_split=""
        for line in list:
            string = re.sub("[^0-9a-zA-Z]", " ", line)
            hyphen_split += string.replace(' ','-')

        #print(hypen_split,end="")
        #print()

    def semicolon():
        global semicolon_replace
        list = open("text1.txt", 'r')
        string=list.read()
        semicolon_replace = string.replace('\n', ';')

        # print(semicolon, end="")
        # print()

    def file():
        with open('newfile.txt', 'w+') as f:
            f.write('PREFIX COUNT = %s\n' %count_prefix)
            f.write('\n')
            f.write('SUFFIX COUNT = %s\n' % count_suffix)
            f.write('\n')
            f.write('MAXIMUM REPEATED WORD = %s\n' % maximum_word)
            f.write('\n')
            f.write('PALINDROMIC WORD = %s\n' % palindrome_word)
            f.write('\n')
            f.write('SPLIT WITH VOWELS = ')
            for items in vowels_split:
                f.write('%s'%items)
            f.write('\n\n')
            f.write('CAPITALIZE THIRD LETTER = \n')
            for items in capitalize_3rdletter:
                f.write('%s' % items)
            f.write('\n\n')

            f.write('CAPITALIZE FIFTH WORD = \n')
            for items in capital_5thword:
                f.write('%s' % items)
            f.write('\n\n')

            f.write('REPLACE SPACE BY HYPHEN = \n')
            for items in hyphen_split:
                f.write('%s' % items)
            f.write('\n\n')

            f.write('REPLACE NEWLINE BY SEMICOLON = \n')
            for items in semicolon_replace:
                f.write('%s' % items)
            f.write('\n\n')



    prefix()
    suffix()
    maximumword()
    palindrome()
    uniqueList()
    dictWord()
    vowels()
    capitalize_thirdletter()
    capitalize_5thword()
    hypen()
    semicolon()
    file()

except ZeroDivisionError as err:
   print('Handling run-time error:', err)

except ValueError:
  print("Oops!  That was no valid input.  Try again...")

except:
    print("Unexpected error:", sys.exc_info()[0])






