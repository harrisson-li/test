import unittest

from test_1 import TestPages


def suite1():
    suite = unittest.TestSuite()
    suite.addTest(TestPages('test_etown'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite1())
