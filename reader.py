class FileReader(object):
    def __init__(self):
        self.line = []
        self.list_of_dictionaries = []

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

