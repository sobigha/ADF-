import re
import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

list1=[]
class class_program:
    def __init__(self,file):
        self.file=file

    def read_file(self):

        list = open(file, 'r')
        for line in list:
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for word in string:
                if (word != ""):
                    list1.append(word)

    def write_file(self,items):
         with open(output_file, 'a') as f:
            f.write('%s\n' %items)
         f.close()

class child(class_program):

    def __init__(self,file):
        super().__init__(file)

    def prefix(self):
        self.read_file()      #read_file
        result = []
        count_prefix=0
        for word in list1:
            if word.startswith("to"):
                result.append(word)
                count_prefix = count_prefix + 1
        self.print_file(count_prefix)
        self.write_file(count_prefix)
        logging.info("Prefix method:  %s"%count_prefix)

    def suffix(self):
        result = []
        count_suffix=0
        for word in list1:
            if word.endswith("ing"):
                result.append(word)
                count_suffix = count_suffix + 1
        self.print_file(count_suffix)
        self.write_file(count_suffix)
        logging.debug("Suffix method: %s"%count_suffix)

    def maximumword(self):
        counter = 0
        maximum_word=""
        for i in list1:
            curr_frequency = list1.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                maximum_word = i
        self.print_file(maximum_word)
        self.write_file(maximum_word)
        logging.debug("Maximum method: %s"%maximum_word)

    def palindrome(self):
        palindrome_word=[]
        for i in list1:
            if (i == i[::-1]):
                palindrome_word.append(i)
        self.print_file(palindrome_word)
        self.write_file(palindrome_word)
        logging.debug("Palindrome method: %s"%palindrome_word)

    def uniqueList(self):
        unique = []
        for x in list1:
            if x not in unique:
                unique.append(x)
        self.print_file(unique)
        self.write_file(unique)
        logging.debug("Unique List method: %s"%unique)

    def dictWord(self):
        dict_word = []
        for element in enumerate(list1):
            dict_word.append(element)
        self.print_file(dict_word)
        self.write_file(dict_word)
        logging.debug("Dict Word method: %s"%dict_word)

    def vowels(self):
        global vowels_split
        vowels_split = [re.sub("[aeiouAEIOU]", ' ', i) for i in list1]
        for i in vowels_split:
              print(i,end=" ")
        self.write_file(vowels_split)
        logging.debug("Split by vowels method: %s"%vowels_split)

    def capitalize_thirdletter(self):
        capitalize_3rdletter=""
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
                    capitalize_3rdletter += result + ' '

        self.print_file(capitalize_3rdletter)
        self.write_file(capitalize_3rdletter)
        logging.debug("Capitalise third letter method %s"%capitalize_3rdletter)

    def capitalize_5thword(self):
        capital_5thword=""
        for i in range(1, len(list1)):
            result = ""
            if (i % 5 == 0):
                result += list1[i].upper()
            else:
                result += list1[i]
            capital_5thword += result + " "

        self.print_file(capital_5thword)
        self.write_file(capital_5thword)
        logging.debug("Capitalise fifth word method: %s"%capital_5thword)

    def hyphen(self):
        list = open("text1.txt", 'r')
        hyphen_split = ""
        for line in list:
            string = re.sub("[^0-9a-zA-Z]", " ", line)
            hyphen_split += string.replace(' ', '-')

        self.print_file(hyphen_split)
        self.write_file(hyphen_split)
        logging.debug("Hyphen method: %s"%hyphen_split)


    def semicolon(self):
        list = open("text1.txt", 'r')
        string = list.read()
        semicolon_replace = string.replace('\n', ';')
        self.print_file(semicolon_replace)
        self.write_file(semicolon_replace)
        logging.debug("Semicolon method: %s"%semicolon_replace)

    def print_file(self, items):
        print(items)



# file = cfg.file_info["input_filename"]
# output_file = cfg.file_info["output_filename"]

file=str(input("Enter the file name: "))
output_file=str(input("Enter the output file name: "))
n=int(input("If you want to clear previous contents press 1:"))
if(n==1):
  open(output_file, 'w').close()

x = child(file)
x.prefix()
x.suffix()
x.maximumword()
x.palindrome()
x.uniqueList()
x.dictWord()
x.vowels()
x.capitalize_thirdletter()
x.capitalize_5thword()
x.hyphen()
x.semicolon()
