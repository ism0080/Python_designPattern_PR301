import re
from datetime import date


class Validator(object):

    def __init__(self):
        self.regDic = {"id": r'^[A-Z][0-9]{3}$',
                       "gender": r'^M$|^F$',
                       "age": r'^[0-9]{2}$',
                       "sales": r'^[0-9]{3}$',
                       "bmi": r'(^Normal$|^Overweight$|^Obesity$|^Underweight$)',
                       "salary": r'^[0-9]{2,3}$',
                       "birthday": r'^[0-31]\w-[0-12]\w-[0-9]{4}$'}
        self.dictionary = {}
        self.list_of_dictionaries = []
        self.file_count = 1

    def valid(self, filename):
        invalid = []
        self.dictionary = {}
        try:
            print("\nFILE_DATA:", self.file_count)
            for key, value in filename.items():
                match = re.search(self.regDic.get(key), value)
                if match is not None:
                    if self.valid_date(filename["birthday"]):
                        if int(self.valid_age(filename["birthday"]))\
                                == int(filename["age"]):
                            self.dictionary[key] = value
                        else:
                            raise Exception("Age does not match birthdate")
                    else:
                        break
                else:
                    invalid.extend(["{} = False".format(key.upper())])
            if len(self.dictionary) < 7:
                raise Exception("Data is invalid")
        except Exception as err:
            print("The exception is:", err)
            self.dictionary = {}
        finally:
            self.file_count += 1
            if self.dictionary:
                print(self.dictionary, "\nVALIDATION SUCCESSFUL")
                self.list_of_dictionaries.extend([self.dictionary])
            else:
                print(filename, "\n", invalid, "\nVALIDATION FAILED")

    def valid_date(self, mydate):
        minyear = 1900
        maxyear = date.today().year

        mydate = mydate
        dateparts = mydate.split('-')
        try:
            if int(dateparts[2]) > maxyear or int(dateparts[2]) < minyear:
                raise ValueError("Year out of range")
            dateobj = date(int(dateparts[2]),
                           int(dateparts[1]),
                           int(dateparts[0]))
            return True
        except ValueError as err:
            self.dictionary = {}
            print(err)

    def valid_age(self, mydate):
        today = date.today()
        dateparts = mydate.split('-')
        born = date(int(dateparts[2]), int(dateparts[1]), int(dateparts[0]))
        age = today.year - born.year\
            - ((today.month, today.day) < (born.month, born.day))
        return age

    def get(self):
        return self.list_of_dictionaries
