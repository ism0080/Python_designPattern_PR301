from abc import ABCMeta, abstractmethod
import csv

# class FileReader(object):
#     def __init__(self):
#         self.line = []
#         self.list_of_dictionaries = []
#
#     def read(self, filename):
#         try:
#             with open(filename, 'r') as file:
#                 file_data = file.read()
#                 new_line_split = file_data.split('\n')
#
#                 self.splits_on_comma_separation(new_line_split)
#                 self.create_list_of_dictionaries()
#
#             return self.list_of_dictionaries
#         except IOError as err:
#             print("The exception is: ", err)
#             pass
#
#     def create_list_of_dictionaries(self):
#         for empty in self.list_of_dictionaries:
#             self.list_of_dictionaries[empty] \
#                 = dict(e.split('=') for e in self.line[empty])
#
#     def splits_on_comma_separation(self, new_line_split):
#         i = 0
#         for x in new_line_split:
#             self.line.extend([new_line_split[i].split(', ')])
#             self.list_of_dictionaries.extend([i])
#             i += 1


class FileReader(object):
    def __init__(self, file_type):
        self.file_type = file_type

    def read_file(self, file):
        return self.file_type.read(file)


class AbstractReader(metaclass=ABCMeta):
    def __init__(self):
        self.line = []
        self.list_of_dictionaries = []

    @abstractmethod
    def read(self, filename):
        pass


class TextFileReader(AbstractReader):
    def __init__(self):
        super().__init__()

    def read(self, filename):
        try:
            with open(filename, 'r') as file:
                file_data = file.read()
                new_line_split = file_data.split('\n')

                self.splits_on_comma_separation(new_line_split)
                self.create_list_of_dictionaries()

            return self.list_of_dictionaries
        except IOError as err:
            print("The exception is: ", err)
            pass

    def create_list_of_dictionaries(self):
        for empty in self.list_of_dictionaries:
            self.list_of_dictionaries[empty] \
                = dict(e.split('=') for e in self.line[empty])

    def splits_on_comma_separation(self, new_line_split):
        i = 0
        for x in new_line_split:
            self.line.extend([new_line_split[i].split(', ')])
            self.list_of_dictionaries.extend([i])
            i += 1


class CSVReader(AbstractReader):
    def __init__(self):
        super().__init__()

    def read(self, filename):
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_dict = {'id': row['Empid'],
                              'gender': row['Gender'],
                              'age': row['Age'],
                              'sales': row['Sales'],
                              'bmi': row['BMI'],
                              'salary': row['Salary'],
                              'birthday': row['Birthday']}

                self.list_of_dictionaries.extend([data_dict])
        return self.list_of_dictionaries
