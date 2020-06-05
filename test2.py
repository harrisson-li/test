from selenium import webdriver


class EtownPage:


    driver = webdriver.Chrome()
    user_name = driver.find_element_by_xpath(USER_NAME)
    password = driver.find_element_by_xpath(PASSWORD)
    submit = driver.find_element_by_xpath(SUBMIT)
