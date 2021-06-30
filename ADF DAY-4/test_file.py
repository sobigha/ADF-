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
        with open("text1.txt", 'r') as list1:
            line = list1.readlines()
            return line

    @classmethod
    def write_file(cls,items):
        """Write the output to the file"""
        with open("newfile.txt", 'a') as file_write:
            file_write.write('%s\n' %items)
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


<<<<<<< HEAD
    # def test_toprefix(self):
    #     """Check if both results are true"""
    #     res1 = self.prefix_word()
    #     res2 = ['to', 'together']
    #     assert res1 == res2
=======
    def test_toprefix(self):
        """Check if both results are true"""
        res1 = self.prefix_word()
        res2 = ['to', 'together']
        assert res1 == res2
>>>>>>> e25c06fdc6fe739ed7a7c5209f7c4f1a6ee5ec9c


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

<<<<<<< HEAD
    # def test_suffix(self):
    #     """Check if both results are true"""
    #     result_first = self.suffix_word()
    #     result_check = ['coming', 'going']
    #     assert result_first == result_check
=======
    def test_suffix(self,):
        """Check if both results are true"""
        result_first = self.suffix_word()
        result_check = ['coming', 'going']
        assert result_first == result_check
>>>>>>> e25c06fdc6fe739ed7a7c5209f7c4f1a6ee5ec9c

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
        logging.debug("Maximum method: %s",maximum_word)
        return maximum_word

    # def test_maximum(self):
    #     """Check if both results are true"""
    #     result_first = self.maximum_words()
    #     result_check = 'cab'
    #     assert result_first == result_check

    def palindrome_words(self):
        """Return all the palindromic word"""
        palindrome_word=[]
        result=[]
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
        logging.debug("Palindrome method: %s",palindrome_word)
        return palindrome_word

    # def test_palindrome(self):
    #     """Check if both results are true"""
    #     result_first = self.palindrome_words()
    #     result_check = ['madam']
    #     assert result_first == result_check

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
        logging.debug("Unique List method: %s",unique)
        return unique

    # def test_unique(self):
    #     """Check if both results are true"""
    #     result_first = self.unique_list()
    #     result_check = ['to', 'together', 'coming', 'going', 'cab', 'madam']
    #     assert result_first == result_check


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
        logging.debug("Dict Word method: %s",dict_word)
        return dict_word

    # def test_dictword(self):
    #     """Check if both results are true"""
    #     result_first = self.dict_word()
    #     result_check = [(0, 'to'), (1, 'together'), (2, 'coming'), (3, 'going'),\
    #                     (4, 'cab'), (5, 'cab'), (6, 'madam')]
    #     assert result_first == result_check


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
            print(i_iter,end=" ")
            count = count+1
        print(count)

        self.write_file(vowels_split)
        logging.debug("Split by vowels method: %s",vowels_split)
        return count

    # def test_vowels(self):
    #     """Check if both results are true"""
    #     result_first = self.vowels()
    #     result_check = 7
    #     assert result_first == result_check

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
            logging.debug("Capitalise third letter method %s",capitalize_3rdletter)
            return capitalize_3rdletter

    # def test_capitalthird(self):
    #     """Check if both results are true"""
    #     result_first = self.capitalize_thirdletter()
    #     result_check = 'to toGether coMing goIng caB caB maDam '
    #     assert result_first == result_check

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
            logging.debug("Capitalise fifth word method: %s",capital_5thword)
            return capital_5thword

    # def test_capitalfifth(self):
    #     """Check if both results are true"""
    #     result_first = self.capitalize_5thword()
    #     result_check = 'together coming going cab CAB madam '
    #     assert result_first == result_check

    def hyphen(self):
        """Replace hyphen with space"""
        with open("text1.txt", 'r') as list1:
            hyphen_split = ""
            for line in list1:
                string = re.sub("[^0-9a-zA-Z]", " ", line)
                hyphen_split += string.replace(' ', '-')

            self.print_file(hyphen_split)
            self.write_file(hyphen_split)
            logging.debug("Hyphen method: %s",hyphen_split)
            return hyphen_split

    # def test_hyphen(self):
    #     """Check if both results are true"""
    #     result_first = self.hyphen()
    #     result_check = 'to-together-coming-going-cab-cab-madam'
    #     assert result_first == result_check


    def semicolon(self):
        """Replace the semicolon in newline"""
        with open("text1.txt", 'r') as list1:
            string = list1.read()
            semicolon_replace = string.replace('\n', ';')
            self.print_file(semicolon_replace)
            self.write_file(semicolon_replace)
            logging.debug("Semicolon method: %s",semicolon_replace)
            return semicolon_replace

    # def test_semicolon(self):
    #     """Check if both results are correct"""
    #     result_first = self.semicolon()
    #     result_check = 'to together coming going cab cab madam'
    #     assert result_first == result_check

    @classmethod
    def print_file(cls,items):
        """Print items"""
        print(items)


# file = cfg.file_info["input_filename"]
# output_file = cfg.file_info["output_filename"]
#
# file=str(input("Enter the file name: "))
# output_file=str(input("Enter the output file name: "))
# n=int(input("If you want to clear previous contents press 1:"))
# if(n==1):
#   open("newfile.txt", 'w').close()

x = TestChild()
x.prefix_word()
<<<<<<< HEAD
x.suffix_word()
=======
# x.test_toprefix()
x.suffix_word()
# x.test_suffix(res)
>>>>>>> e25c06fdc6fe739ed7a7c5209f7c4f1a6ee5ec9c
x.maximum_words()
x.palindrome_words()
x.unique_list()
x.dict_word()
x.vowels()
x.capitalize_thirdletter()
x.capitalize_5thword()
x.hyphen()
x.semicolon()
