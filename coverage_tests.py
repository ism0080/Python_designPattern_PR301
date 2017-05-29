from unit_tests import *
from more_tests import *


import unittest


def my_suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(MainTests))
    the_suite.addTest(unittest.makeSuite(MoreTests))

    return the_suite

if __name__ == "__main__":  # pragma: no cover
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = my_suite()
    runner.run(test_suite)