import unittest

import test_1
from test_1 import TestPages


def suite1():
    suite = unittest.TestSuite()
    suite.addTest(TestPages('test_assert'))
    suite.addTest(TestPages('test_baidu'))
    return suite


def suite3():
    suite = unittest.TestSuite()
    suite.addTests([TestPages('test_assert'), TestPages('test_baidu')])
    return suite


def suite4():
    suite = unittest.TestLoader().discover('.', 'test_1.py')
    return suite


def suite5():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    return suite


def suite6():
    suite = unittest.makeSuite(TestPages, prefix='test_b')
    return suite


def suite7():
    suite = unittest.findTestCases(test_1, prefix='test_b')
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    # suite2 = unittest.TestSuite()
    # suite2.addTest(TestPages('test_assert'))
    # suite2.addTest(TestPages('test_baidu'))

    runner.run(suite7())

    # assert 111 == int('111'), '111 != 111'
    # assert 111 != int('222'), '111 == 222'
