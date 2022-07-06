import logging

logging.basicConfig(filename='string.log',level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')

class String:

    def __init__(self,string):
        self.string = string

    #reverse a string without using reverse function
    def reverse_string(self):
        try:
            logging.info('Reversing string')
            rev_str = self.string[::-1]
            logging.info(rev_str)
            return rev_str
        except Exception as e:
            logging.exception(e)

    #split a string after conversion of entire string in uppercase
    def upper_split(self):
        try:
            logging.info('Converting string')
            upper_split = self.string.upper().split()
            logging.info(upper_split)
            return upper_split
        except Exception as e:
            logging.exception(e)

    #convert the whole string into lower case
    def lower_case(self):
        try:
            logging.info('Converting string to lower case')
            lower = self.string.lower()
            logging.info(lower)
            return lower
        except Exception as e:
            logging.exception(e)

    #capitalize the whole string
    def capitalise(self):
        try:
            logging.info('Capitalising string')
            cap = self.string.capitalize()
            logging.info(cap)
            return cap
        except Exception as e:
            logging.exception(e)

    #Replace a string charecter by another charector
    def replace_char(self,old_char,new_char):
        try:
            logging.info('replacing string character by another one')
            cap = self.string.replace(old_char,new_char)
            logging.info(cap)
            return cap
        except Exception as e:
            logging.exception(e)

    #function which can return a concatination of all the string that we will pass
    def concat(self,*args):
        try:
            logging.info('Concatenating all the strings')
            concat_str = " ".join([i for i in args])
            logging.info(concat_str)
            return concat_str
        except Exception as e:
            logging.exception(e)

    #filter out all the vowels from text by using while loop
    def filter_vowels(self):
        try:
            logging.info('filtering vowels')
            vowels=[]
            i = 0
            while i < len(self.string):
                vowel = ['a', 'e', 'i', 'o', 'u']
                if self.string[i].lower() in vowel:
                    vowels.append(self.string[i])

                i += 1
            logging.info(vowels)
            return vowels
        except Exception as e:
            logging.exception(e)

    #write a fun which will take string and return a len of
    # it without using a inbuilt fun len

    def len_string(self):
        try:
            logging.info('calculating string length')
            count = 0
            for i in self.string:
                count += 1
            logging.info(count)
            return count
        except Exception as e:
            logging.exception(e)

if __name__ == '__main__':

    obj = String('My name is Abhishek Mishra and MAANG is my dream.')
    print(obj.reverse_string())
    print(obj.upper_split())
    print(obj.lower_case())
    print(obj.capitalise())
    print(obj.replace_char('dream','important dream'))
    print(obj.concat('This','is','dynamic','args','function'))
    print(obj.filter_vowels())
    print(obj.len_string())


