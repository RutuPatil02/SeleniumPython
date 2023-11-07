from Base import InitiateDriver
from Library import ConfigReader


def test_InvalidRegistration():
    driver = InitiateDriver.start_browser()
    driver.find_element('name', ConfigReader.Read_Elements('Registration','U_Pass')).send_keys('pass')
    driver.find_element('name', ConfigReader.Read_Elements('Registration','Conf_Pass')).send_keys('pass')
    driver.find_element('name', ConfigReader.Read_Elements('Registration','Phone_No')).send_keys('123456')
    InitiateDriver.close_browser(driver)