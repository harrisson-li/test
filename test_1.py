import time
import unittest

from selenium import webdriver

from test_2 import EtownPage, BaiduPage


class Container:
    driver = None
    pass


instance = Container()


class TestPages(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        instance.driver = driver

    def tearDown(self):
        driver = instance.driver
        driver.quit()

    def test_etown(self):
        driver = instance.driver
        driver.get('https://qa.englishtown.cn/partner/englishcenters')

        driver.find_element_by_xpath(EtownPage.USER_NAME).send_keys('stestc16569')
        driver.find_element_by_xpath(EtownPage.PASSWORD).send_keys('1')
        driver.find_element_by_xpath(EtownPage.SUBMIT).click()

        time.sleep(5)
        self.assertEqual(driver.find_element_by_xpath(EtownPage.STUDENT_NAME).text, 's14hz!')

    def test_baidu(self):
        driver = instance.driver
        driver.get('https://www.baidu.com/')

        driver.find_element_by_xpath(BaiduPage.CONTENT).send_keys('python')
        driver.find_element_by_xpath(BaiduPage.SEARCH).click()

        time.sleep(5)

    def test_assert(self):
        self.assertEqual(111, int('111'), '111 != int(\'111\')')
        self.assertNotEqual(111, int('222'), '111 == int(\'222\')')


# class TestBaidu(unittest.TestCase):
#     driver = webdriver.Chrome()
#     driver.get('https://www.baidu.com/')
#
#     driver.find_element_by_xpath(CONTENT).send_keys('python')
#     driver.find_element_by_xpath(SEARCH).click()
#
#     time.sleep(5)
#     driver.close()


if __name__ == '__main__':
    unittest.main()
