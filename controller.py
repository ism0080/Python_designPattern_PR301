from validator import Validator
from database import DatabaseMaker
from reader import FileReader
from display import PyGal


class Controller(object):
    def __init__(self):
        self.val = Validator()
        self.db = DatabaseMaker()
        self.reader = FileReader()
        self.py = PyGal()
        self.converted_file = None
        self.file_count = 1

    def read_file(self, filename):
        try:
            self.converted_file = self.reader.read(filename)
            for dict in self.converted_file:
                print("FILE_DATA:", self.file_count, "\n", dict)
                self.file_count += 1
        except Exception as err:
            print("The exception is: ", err)

    def valid(self, flag):
        try:
            options = {'': self.validate,
                       '-v': self.view_valid,
                       '-f': self.read_validate
                       }
            return options[flag]()
        except Exception as err:
            print("The exception is: ", err, " is not a valid flag")

    def validate(self):
        try:
            for dict in self.converted_file:
                self.val.valid(dict)
        except Exception as err:
            print("The exception is: No file specified")

    def view_valid(self):
        print("\n VALID DATA:")
        for dict in self.val.get():
            print(dict)

    def read_validate(self):
        file = input("Validate which file?:")
        self.read_file(file)
        self.validate()

    def db_table(self, flag):
        try:
            options = {'': self.db_view,
                       '-d': self.db_drop_table,
                       '-c': self.db_create_table,
                       '-dc': self.db_drop_create_table,
                       '-i': self.db_insert_flag,
                       '-if': self.db_database_read_validate_insert
                       }
            return options[flag]()
        except Exception as err:
            print("The exception is: ", err)

    def db_drop_table(self):
        self.db.drop_table("employee")

    def db_create_table(self):
        self.db.create_table()

    def db_drop_create_table(self):
        self.db_drop_table()
        self.db_create_table()
        return True

    def db_insert_flag(self):
        for i in self.db_insert():
            print(i)

    def db_database_read_validate_insert(self):
        self.read_validate()
        self.db_insert()

    def db_insert(self):
        try:
            list_of_dictionaries = self.val.get()
            if list_of_dictionaries:
                for dict in list_of_dictionaries:
                    self.db.insert(dict["id"],
                                   dict["gender"],
                                   dict["age"],
                                   dict["sales"],
                                   dict["bmi"],
                                   dict["salary"],
                                   dict["birthday"])
                return self.db.get("*")
            else:
                raise Exception("Cannot add invalid data to the database")
        except Exception as err:
            print("The exception is: ", err)

    def db_view(self, value):
        if not value:
            value = input("What column to see from database?")
        for v in self.db.get(value):
            print(v)

    def database_close(self):
        self.db.close()

    def pygal(self, count):
        try:
            display = {}
            for x in range(0, int(count)):
                value = input("What to see from the bar graph?")
                data = self.db.bar_get(value)
                display.update({value: data})
            self.py_view(display)
        except Exception as err:
            print("The exception is: ", err)

    def py_view(self, dictionary):
        try:
            id = self.db.bar_get('id')
            self.py.bar_char(id, dictionary)
            # doesn't reach this exception but there just in case
        except Exception as err:  # pragma: no cover
            print("The exception is: ", err)

    def pickled(self, flag):
        try:
            options = {'': self.pickled_write,
                       '-r': self.pickled_read}
            name = input("Name of pickle file?")
            if name == '':
                raise Exception("Not a valid filename")
            else:
                return options[flag](name)
        except Exception as err:
            print("The exception is: ", err)

    def pickled_write(self, name):
        import pickle
        with open('{name}.pickle'.format(name=name), 'wb') as f:
            pickle.dump(self.converted_file, f)
        return True

    def pickled_read(self, name):
        import pickle
        with open('{name}.pickle'.format(name=name), 'rb') as f:
            data = pickle.load(f)
        print(data)
        # print(data == self.db_view("*"))
