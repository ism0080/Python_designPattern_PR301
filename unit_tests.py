import unittest
import reader
import database
import validator


class MainTests(unittest.TestCase):
    def setUp(self):
        self.read = reader.FileReader()
        self.valid = validator.Validator()
        self.db = database.DatabaseMaker()

    def tearDown(self):
        print("down")

    def test_isRead_FileIsValidFormat_IsEqual(self):
        print("Check if file is valid format")
        testData = [{'id': 'A123', 'gender': 'M', 'age': '20', 'sales': '123', 'bmi': 'Normal', 'salary': '109', 'birthday': '24-10-1996'}]
        r = self.read.read("table.txt")
        self.assertEqual(r, testData, 'Not a valid file')

    def test_isRead_FileIsNotValidFormat_IsFalse(self):
        print("Check if file is invalid format")
        testData = [{'id': 'A123', 'gender': 'M', 'age': '20', 'sales': '001', 'bmi': 'Overweight', 'salary': '44', 'birthday': '02-02-2000'}]
        r = self.read.read("table2.txt")
        self.assertFalse(r == testData, 'Is a valid file')

    def test_isValid_CheckAge_IsEqual(self):
        print("Check if age can be found")
        age = self.valid.valid_age('24-10-1996')
        self.assertEqual(age, 20, 'Age doesn"t match')

    def test_isNotValid_CheckAge_IsNotEqual(self):
        print("Check if age can be found")
        age = self.valid.valid_age('24-10-1994')
        self.assertNotEqual(age, 25, 'Age doesn"t match')

    def test_isValid_CheckDate_IsTrue(self):
        print("Is date valid")
        date = self.valid.valid_date('24-10-1996')
        self.assertTrue(date == True, 'Date isn"t true')

    def test_isNotValid_CheckDate_IsFalse(self):
        print("Is date invalid")
        date = self.valid.valid_date('31-02-1996')
        self.assertFalse(date == False, 'Date isn"t false')

    def test_isValid_CheckAgeAgainstDate_IsEqual(self):
        print("Check if age matches date from testData")
        testData = {'id': 'A123', 'gender': 'M', 'age': '20', 'sales': '123', 'bmi': 'Normal', 'salary': '109',
                     'birthday': '24-10-1996'}
        age = self.valid.valid_age('24-10-1996')
        self.assertEqual(age, int(testData['age']), 'Age doesn"t match')

    def test_isNotValid_CheckAgeAgainstDate_IsNotEqual(self):
        print("Check if age not matches date from testData")
        testData = {'id': 'A123', 'gender': 'M', 'age': '24', 'sales': '123', 'bmi': 'Normal', 'salary': '109',
                     'birthday': '24-10-1996'}
        age = self.valid.valid_age('24-10-1996')
        self.assertNotEqual(age, int(testData['age']), 'Age doesn"t match birthday')

    def test_isValid_InsertDBThenGet_IsEqual(self):
        print("Check if age not matches age from database")
        self.db.drop_table('employee')
        self.db.create_table()
        self.db.insert('A123', 'M', '20', '123', 'Normal', '109', '24-10-1996')
        data = self.db.get('age')
        self.assertEqual(data, [(20,)], 'Not equal')

    def test_isValid_InsertDBThenGetMoreThanOneRow_IsEqual(self):
        print("Check if ages not match ages from database")
        self.db.drop_table('employee')
        self.db.create_table()
        self.db.insert('A123', 'M', '20', '123', 'Normal', '109', '24-10-1996')
        self.db.insert('A124', 'M', '21', '123', 'Normal', '109', '24-10-1996')
        self.db.insert('A125', 'M', '22', '123', 'Normal', '109', '24-10-1996')
        self.db.insert('A126', 'M', '23', '123', 'Normal', '109', '24-10-1996')
        data = self.db.get('age')
        self.assertEqual(data, [(20,),(21,),(22,),(23,)], 'Not equal')

    def test_isValid_DropDBNoData_IsNotEqual(self):
        print("Check if age not matches age from database")
        self.db.drop_table('employee')
        self.db.create_table()
        self.db.insert('A123', 'M', '20', '123', 'Normal', '109', '24-10-1996')
        self.db.drop_table('employee')
        self.db.create_table()
        data = self.db.get('age')
        self.assertNotEqual(data, [(20,)], 'Not equal')

    if __name__ == "__main__":  # pragma: no cover
        unittest.main(verbosity=True)  # with more detail
        # unittest.main()
        # unittest.main(exit=False) # with more detail
