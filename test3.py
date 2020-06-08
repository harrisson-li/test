from test1 import TestPages
import unittest


def suite1():
    suite = unittest.TestSuite()
    suite.addTest(TestPages('test_etown'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite1())