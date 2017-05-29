"""
Problem Domain CMD
"""
import sys
from cmd import Cmd

class DomainCmd(Cmd):
    """
    single command processor example
    """

    def __init__(self, con):
        Cmd.__init__(self)
        self.prompt = "-> "
        self.intro = "Welcome to the Problem Domain"
        self.con = con

    # Support Command-Line Argument
    def arg(self):
        try:
            if sys.argv[1] == "chart":
                self.do_chart(sys.argv[2])
            if sys.argv[1] == "read":
                self.do_read(sys.argv[2])
            if sys.argv[1] == "validate":
                self.do_validate(sys.argv[2])
            if sys.argv[1] == "db":
                self.do_db(sys.argv[2])
        except Exception as err:
            pass

    # Read the file
    def do_read(self, filename):
        """
        Syntax: read [filename.extension]
            read the file and convert to dictionary format
        :param filename:
        :return: Contents of the file
        """
        if filename:
            self.con.read_file(filename)
        else:
            print("Enter a filename")

    # Validate the file
    def do_validate(self, flag):
        """
        Syntax: validate [flag]
            validate: will validate the previously read file
            validate -f: will ask which file to read and validate
            validate -v: will show which data was valid
            validate -fv: will ask which file to read and
                          validate and will show which data was valid
        :param flag: -f, -v, -fv
        :return: Each file and whether it was valid or not
        """
        self.con.valid(flag)

    # Input/Output of Database
    def do_db(self, flag):
        """
        Syntax: db [flag]
            db: asks which column you would like to see from the table
            db -i: inserts the previously validated data
            db -if: asks which file you would like to input to the database,
                    reads it, validates, then inserts
            db -d: drop table
            db -c: create table
            db -dc: drop and create table
        :param flag: -i, -if, -v, -d, -c, -dc
        :return: Database knowledge
        """
        self.con.db_table(flag)

    # PyGal Chart
    def do_chart(self, count):
        """
        Syntax: chart [count]
            chart: enter a the number of values that you want to see in the chart
                    from the database. Then asks which column from the table you
                    want to display in a barchart (age, sales, salary)
        :param count: 'a number'
        :return: Opens web browser to display barchart
        """
        self.con.pygal(count)

    # Pickle Serial
    def do_serial(self, flag):
        """
        Syntax: serial [flag]
            serial: writes the contents of the recently read file to [yourfilename].pickle
                    you will be prompted for the name of the pickle file
            serial -r: reads the contents of 'data.pickle'
        :param flag: -r
        :return: contents of 'data.pickle'
        """
        self.con.pickled(flag)

    # Quit the cmd
    def do_quit(self, line):
        """
        Syntax: quit
            quit from my CMD
        :return: True
        """
        self.con.database_close()
        print("Closing cmd..")
        return True

    # shortcut
    do_q = do_quit
