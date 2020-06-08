from selenium import webdriver
import time
import unittest

USER_NAME = "//input[@name='username']"
PASSWORD = "//input[@name='password']"
SUBMIT = "//button[@type='submit']"

CONTENT = "//input[@name='wd']"
SEARCH = "//input[@type='submit']"


class Container:
    driver = None
    pass


instance = Container()


class TestPages(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        instance.driver = driver

    def tearDown(self):
        driver = instance.driver
        driver.quit()

    def test_etown(self):
        driver = instance.driver
        driver.get('https://qa.englishtown.cn/partner/englishcenters')

        driver.find_element_by_xpath(USER_NAME).send_keys('stestc9445')
        driver.find_element_by_xpath(PASSWORD).send_keys('1')
        driver.find_element_by_xpath(SUBMIT).click()

        time.sleep(5)

    def test_baidu(self):
        driver = instance.driver
        driver.get('https://www.baidu.com/')

        driver.find_element_by_xpath(CONTENT).send_keys('python')
        driver.find_element_by_xpath(SEARCH).click()

        time.sleep(5)


# class TestBaidu(unittest.TestCase):
#     driver = webdriver.Chrome()
#     driver.get('https://www.baidu.com/')
#
#     driver.find_element_by_xpath(CONTENT).send_keys('python')
#     driver.find_element_by_xpath(SEARCH).click()
#
#     time.sleep(5)
#     driver.close()


# if __name__ == '__main__':
#     unittest.main()
