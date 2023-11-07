from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver import Firefox
from Library import ConfigReader


def start_browser():
    global driver
    if ConfigReader.Read_ConfigFile('Details','Browser') == 'Chrome':
        driver = Chrome()
    elif ConfigReader.Read_ConfigFile('Details','Browser') == 'Edge':
        driver = Edge()
    elif ConfigReader.Read_ConfigFile('Details','Browser') == 'Firefox':
        driver = Firefox()
    else:
        driver = Chrome()

    driver.get(ConfigReader.Read_ConfigFile('Details', 'ApplicationURL'))
    driver.maximize_window()
    return driver


def close_browser(driver):
     driver.close()
