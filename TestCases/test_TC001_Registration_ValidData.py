from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest
from DataGenerate import DataGen


# parametrize fetches 1 list from list 'li' at a time [Data driven testing]
@pytest.mark.parametrize('data', DataGen.dataGenerator())
def test_ValidRegistration(data):
    driver = InitiateDriver.start_browser()
    register = RegistrationPage.RegistrationClass(driver)

    driver.find_element('name', ConfigReader.Read_Elements('Registration', 'User_Name')).send_keys('Rutuja')
    driver.find_element('name', ConfigReader.Read_Elements('Registration', 'U_Pass')).send_keys('rutu')

    # data from excel file [Data driven testing]
    # register.enter_username(data[0])
    # register.enter_pswd(data[1])

    InitiateDriver.close_browser(driver)
