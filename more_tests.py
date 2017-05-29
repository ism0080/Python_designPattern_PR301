import unittest
import reader
import database
import command_line
import validator
import display
import controller
import mock
import sys
import io


class MoreTests(unittest.TestCase):
    def setUp(self):
        self.read = reader.FileReader()
        self.valid = validator.Validator()
        self.db = database.DatabaseMaker()
        self.con = controller.Controller()
        self.cmd = command_line.DomainCmd(self.con)
        self.chart = display.PyGal()

    def tearDown(self):
        print("down")

    def test_database_duplicate_data_exception_thrown(self):
        self.db.insert('A123', 'M', '20', '123', 'Normal', '109', '24-10-1996')
        self.assertRaises(Exception,  self.db.insert('A123', 'M', '20', '123', 'Normal', '109', '24-10-1996'))

    def test_database_noSuchTableData_exceptionThrown(self):
        self.assertRaises(Exception, self.db.get("Dog"))

    def test_database_bar_get(self):
        self.db.drop_table("employee")
        self.db.create_table()
        self.db.insert('A123', 'M', '20', '123', 'Normal', '109', '24-10-1996')
        self.assertEqual(["M"], self.db.bar_get("gender"), 'Not Equal')

    def test_database_bar_get_exception_thrown(self):
        self.assertRaises(Exception, self.db.bar_get("Dog"))

    def test_cmd_read_noFilename(self):
        captured = io.StringIO()
        sys.stdout = captured
        self.cmd.do_read("")

        expected = "Enter a filename\n"
        actual = captured.getvalue()

        self.assertEqual(expected, actual)

    def test_cmd_read(self):
        captured = io.StringIO()
        sys.stdout = captured
        self.cmd.do_read("table.txt")

        expected = "FILE_DATA: 1 \n {'id': 'A123', 'gender': 'M', 'age': '20', 'sales': '123', 'bmi': 'Normal'," \
                   " 'salary': '109', 'birthday': '24-10-1996'}\n"
        actual = captured.getvalue()

        self.assertEqual(expected, actual)

    def test_cmd_read_invalidFile(self):
        self.assertRaises(Exception, self.cmd.do_read("invalid.txt"))

        # def test_con_validator(self):
        #     testFile = self.con.read_file("testData.txt")
        #     test = self.con.validate()

    def test_cmd_validator_throw_exception(self):
        self.assertRaises(Exception, self.cmd.do_validate(''))

    def test_validator_get(self):
        self.assertEqual([], self.valid.get())

    def test_cmd_validator_invalidFlag(self):
        self.assertRaises(Exception, self.cmd.do_validate('-c'))

    def test_cmd_validator(self):
        self.cmd.do_read('table.txt')
        captured = io.StringIO()
        sys.stdout = captured
        self.cmd.do_validate('')

        expected = "\nFILE_DATA: 1\n{'id': 'A123', 'gender': 'M', 'age': '20', 'sales': '123', 'bmi': 'Normal'," \
                   " 'salary': '109', 'birthday': '24-10-1996'} \nVALIDATION SUCCESSFUL\n"
        actual = captured.getvalue()

        self.assertEqual(expected, actual)

    def test_cmd_validator_viewValid(self):
        self.cmd.do_read('table.txt')
        self.cmd.do_validate('')
        captured = io.StringIO()
        sys.stdout = captured
        self.cmd.do_validate('-v')

        expected = "\n VALID DATA:\n{'id': 'A123', 'gender': 'M', 'age': '20', 'sales': '123', 'bmi': 'Normal'," \
                   " 'salary': '109', 'birthday': '24-10-1996'}\n"
        actual = captured.getvalue()

        self.assertEqual(expected, actual)

    def test_cmd_validator_readValidate(self):
        captured = io.StringIO()
        sys.stdout = captured
        with mock.patch('controller.input') as mp:
            mp.return_value = "table.txt"
            self.cmd.do_validate('-f')

        expected = "FILE_DATA: 1 \n {'id': 'A123', 'gender': 'M', 'age': '20', 'sales': '123', 'bmi': 'Normal', " \
                   "'salary': '109', 'birthday': '24-10-1996'}\n\n" \
                   "FILE_DATA: 1\n{'id': 'A123', 'gender': 'M', 'age': '20', 'sales': '123', 'bmi': 'Normal', " \
                   "'salary': '109', 'birthday': '24-10-1996'} \nVALIDATION SUCCESSFUL\n"
        actual = captured.getvalue()

        self.assertEqual(expected, actual)

    def test_cmd_pickled_write(self):
        with mock.patch('controller.input') as mp:
            mp.return_value = "data"
            self.assertTrue(self.con.pickled(''))

    def test_cmd_pickled_read(self):
        captured = io.StringIO()
        sys.stdout = captured
        with mock.patch('controller.input') as mp:
            mp.return_value = "data"
            self.con.pickled('-r')

        expected = "None\n"
        actual = captured.getvalue()

        self.assertEqual(expected, actual)

    def test_cmd_pickled_notValidFilename(self):
        with mock.patch('controller.input') as mp:
            mp.return_value = ""
            self.assertRaises(Exception, self.con.pickled(''))

    def test_cmd_chart(self):
        with mock.patch('controller.input') as mp:
            mp.return_value = "sales"
            self.cmd.do_chart(2)

    def test_cmd_chart_invalid(self):
        self.assertRaises(Exception, self.cmd.do_chart(''))

    def test_cmd_database_droptable(self):
        self.assertTrue(self.con.db_table('-dc'))

    def test_con_database_throwException(self):
        self.assertRaises(Exception, self.con.db_table('q'))

    def test_con_pygal_throwException(self):
        self.assertRaises(Exception, self.con.py_view(123))

    def test_cmd_arg_throwException(self):
        sys.argv = "cart"
        self.assertRaises(Exception, self.cmd.arg())

    if __name__ == "__main__":  # pragma: no cover
        unittest.main(verbosity=True)  # with more detail
        # unittest.main()
        # unittest.main(exit=False) # with more detail
