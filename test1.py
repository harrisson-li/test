from selenium import webdriver
import time
import unittest

USER_NAME = "//input[@name='username']"
PASSWORD = "//input[@name='password']"
SUBMIT = "//button[@type='submit']"

CONTENT = "//input[@name='wd']"
SEARCH = "//input[@type='submit']"


class TestEtown(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.get('https://qa.englishtown.cn/partner/englishcenters')

    driver.find_element_by_xpath(USER_NAME).send_keys('stestc9445')
    driver.find_element_by_xpath(PASSWORD).send_keys('1')
    driver.find_element_by_xpath(SUBMIT).click()

    time.sleep(5)
    driver.close()


class TestBaidu(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')

    driver.find_element_by_xpath(CONTENT).send_keys('python')
    driver.find_element_by_xpath(SEARCH).click()

    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    unittest.main()
