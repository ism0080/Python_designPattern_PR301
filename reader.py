from abc import ABCMeta, abstractmethod
import csv


class FileReader(object):
    def __init__(self, file_type):
        self.file_type = file_type

    def read_file(self, file):
        return self.file_type.read(file)


class AbstractReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self, filename):
        pass


class TextFileReader(AbstractReader):
    def __init__(self):
        self.__line = []
        self.__list_of_dictionaries = []

    def read(self, filename):
        try:
            with open(filename, 'r') as file:
                file_data = file.read()
                new_line_split = file_data.split('\n')

                self.__splits_on_comma_separation(new_line_split)
                self.__create_list_of_dictionaries()

            return self.__list_of_dictionaries
        except IOError as err:
            print("The exception is: ", err)
            pass

    def __create_list_of_dictionaries(self):
        for empty in self.__list_of_dictionaries:
            self.__list_of_dictionaries[empty] \
                = dict(e.split('=') for e in self.__line[empty])

    def __splits_on_comma_separation(self, new_line_split):
        i = 0
        for x in new_line_split:
            self.__line.extend([new_line_split[i].split(', ')])
            self.__list_of_dictionaries.extend([i])
            i += 1


class CSVReader(AbstractReader):
    def __init__(self):
        self.__list_of_dictionaries = []

    def read(self, filename):
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile)
                self.__create_list_of_dictionaries(reader)

            return self.__list_of_dictionaries
        except IOError as err:
            print("The exception is: ", err)
            pass

    def __create_list_of_dictionaries(self, reader):
        for row in reader:
            data_dict = {'id': row['Empid'],
                         'gender': row['Gender'],
                         'age': row['Age'],
                         'sales': row['Sales'],
                         'bmi': row['BMI'],
                         'salary': row['Salary'],
                         'birthday': row['Birthday']}

            self.__list_of_dictionaries.extend([data_dict])