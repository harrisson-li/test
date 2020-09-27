class EtownPage:
    USER_NAME = "//input[@name='username']"
    PASSWORD = "//input[@name='password']"
    SUBMIT = "//button[@type='submit']"

    STUDENT_NAME = "//div[@class='welcome-left']/b"


class BaiduPage:
    CONTENT = "//input[@name='wd']"
    SEARCH = "//input[@type='submit']"

    # driver = webdriver.Chrome()
    # user_name = driver.find_element_by_xpath(USER_NAME)
    # password = driver.find_element_by_xpath(PASSWORD)
    # submit = driver.find_element_by_xpath(SUBMIT)
