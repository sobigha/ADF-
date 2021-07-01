"""Program to implement pytest"""
import re
import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)


class TestClassprogram:
    """
    Class to read input from file
    Write contents to the file
    """

    @classmethod
    def read_file(cls):
        """Read the lines from file"""
        with open(FILE, 'r') as list1:
            line = list1.readlines()
            return line

    @classmethod
    def write_file(cls, items):
        """Write the output to the file"""
        with open(OUTPUT, 'a') as file_write:
            file_write.write('%s\n' % items)
            file_write.close()


# pylint: disable=R0904
class TestChild(TestClassprogram):
    """
     Child class inherits the parent class
     Implements functions
    """

    def prefix_word(self):
        """Return the word beginning wth prefix 'to'"""
        list2 = self.read_file()
        result = []
        count_prefix = 0
        for word in list2:
            string = re.sub("[^a-zA-Z0-9]", " ", word).split(" ")
            for s1_iter in string:
                if s1_iter != "":
                    if s1_iter.startswith("to"):
                        result.append(s1_iter)
                        count_prefix = count_prefix + 1

        print(result)
        self.print_file(count_prefix)
        self.write_file(count_prefix)
        logging.debug("Prefix method %s", count_prefix)
        return result

    def suffix_word(self):
        """Return the word ending wth suffix 'ing'"""
        list2 = self.read_file()  # read_file
        result = []
        count_suffix = 0
        for word in list2:
            string = re.sub("[^a-zA-Z0-9]", " ", word).split(" ")
            for s1_iter in string:
                if s1_iter != "":
                    if s1_iter.endswith("ing"):
                        result.append(s1_iter)
                        count_suffix = count_suffix + 1

        print(result)
        self.print_file(count_suffix)
        self.write_file(count_suffix)
        logging.debug("suffix method %s", count_suffix)
        return result

    def maximum_words(self):
        """Return the maximum occured word"""
        list2 = self.read_file()  # read_file
        counter = 0
        result = []
        maximum_word = ""
        for i in list2:
            string = re.sub("[^a-zA-Z0-9]", " ", i).split(" ")
            for s1_iter in string:
                if s1_iter != "":
                    result.append(s1_iter)

            for j in result:
                curr_frequency = result.count(j)
                if curr_frequency > counter:
                    counter = curr_frequency
                    maximum_word = j

        self.print_file(maximum_word)
        self.write_file(maximum_word)
        logging.debug("Maximum method: %s", maximum_word)
        return maximum_word

    def palindrome_words(self):
        """Return all the palindromic word"""
        palindrome_word = []
        result = []
        list2 = self.read_file()
        for i in list2:
            string = re.sub("[^a-zA-Z0-9]", " ", i).split(" ")
            for s1_iter in string:
                if s1_iter != "":
                    result.append(s1_iter)

        for i in result:
            if i == i[::-1]:
                palindrome_word.append(i)

        self.print_file(palindrome_word)
        self.write_file(palindrome_word)
        logging.debug("Palindrome method: %s", palindrome_word)
        return palindrome_word

    def unique_list(self):
        """Remove duplicates from the list"""
        unique = []
        result = []
        list2 = self.read_file()
        for i in list2:
            string = re.sub("[^a-zA-Z0-9]", " ", i).split(" ")
            for s1_iter in string:
                if s1_iter != "":
                    result.append(s1_iter)

        for x_iter in result:
            if x_iter not in unique:
                unique.append(x_iter)

        self.print_file(unique)
        self.write_file(unique)
        logging.debug("Unique List method: %s", unique)
        return unique

    def dict_word(self):
        """Return a counter index and value for the input"""
        dict_word = []
        result = []
        list2 = self.read_file()
        for i in list2:
            string = re.sub("[^a-zA-Z0-9]", " ", i).split(" ")
            for s1_iter in string:
                if s1_iter != "":
                    result.append(s1_iter)

        for element in enumerate(result):
            dict_word.append(element)

        self.print_file(dict_word)
        self.write_file(dict_word)
        logging.debug("Dict Word method: %s", dict_word)
        return dict_word

    def vowels(self):
        """Split the input by vowels"""
        result = []
        count = 0
        list2 = self.read_file()
        for i in list2:
            string = re.sub("[^a-zA-Z0-9]", " ", i).split(" ")
            for s1_iter in string:
                if s1_iter != "":
                    result.append(s1_iter)

        vowels_split = [re.sub("[aeiouAEIOU]", ' ', i) for i in result]
        for i_iter in vowels_split:
            print(i_iter, end=" ")
            count = count + 1
        print(count)

        self.write_file(vowels_split)
        logging.debug("Split by vowels method: %s", vowels_split)
        return count

    def capitalize_thirdletter(self):
        """Capitalize all third letter of every word"""
        result1 = ""
        capitalize_3rdletter = ""
        with open("text1.txt", 'r') as list1:
            for line in list1:
                string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
                for s_iter in string:
                    if s_iter != "":
                        #  result.append(s)
                        result1 = ""
                        for i in range(1, len(s_iter) + 1):
                            if i == 3:
                                result1 += s_iter[i - 1].upper()
                            else:
                                result1 += s_iter[i - 1]
                        capitalize_3rdletter += result1 + ' '

            self.print_file(capitalize_3rdletter)
            self.write_file(capitalize_3rdletter)
            logging.debug("Capitalise third letter method %s", capitalize_3rdletter)
            return capitalize_3rdletter

    def capitalize_5thword(self):
        """"Capitalize all characters of every fifth word"""
        capital_5thword = ""
        result1 = []
        with open("text1.txt", 'r') as list1:
            for line in list1:
                string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
                for s_iter in string:
                    if s_iter != "":
                        result1.append(s_iter)

            for i in range(1, len(result1)):
                result = ""
                if i % 5 == 0:
                    result += result1[i].upper()
                else:
                    result += result1[i]
                capital_5thword += result + " "

            self.print_file(capital_5thword)
            self.write_file(capital_5thword)
            logging.debug("Capitalise fifth word method: %s", capital_5thword)
            return capital_5thword

    def hyphen(self):
        """Replace hyphen with space"""
        with open("text1.txt", 'r') as list1:
            hyphen_split = ""
            for line in list1:
                string = re.sub("[^0-9a-zA-Z]", " ", line)
                hyphen_split += string.replace(' ', '-')

            self.print_file(hyphen_split)
            self.write_file(hyphen_split)
            logging.debug("Hyphen method: %s", hyphen_split)
            return hyphen_split

    def semicolon(self):
        """Replace the semicolon in newline"""
        with open("text1.txt", 'r') as list1:
            string = list1.read()
            semicolon_replace = string.replace('\n', ';')
            self.print_file(semicolon_replace)
            self.write_file(semicolon_replace)
            logging.debug("Semicolon method: %s", semicolon_replace)
            return semicolon_replace

    @classmethod
    def print_file(cls, items):
        """Print items"""
        print(items)


# file = cfg.file_info["input_filename"]
# output_file = cfg.file_info["output_filename"]

FILE = str(input("Enter the file name: "))
OUTPUT = str(input("Enter the output file name: "))
n = int(input("If you want to clear previous contents press 1:"))
if n == 1:
    open(OUTPUT, 'w').close()

x = TestChild()
x.prefix_word()
x.suffix_word()
x.maximum_words()
x.palindrome_words()
x.unique_list()
x.dict_word()
x.vowels()
x.capitalize_thirdletter()
x.capitalize_5thword()
x.hyphen()
x.semicolon()
