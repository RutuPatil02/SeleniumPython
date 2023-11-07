from Base import InitiateDriver
from Library import ConfigReader
import time

driver = InitiateDriver.start_browser()

# Go to Login menu
driver.find_element("xpath", "//label[text()='Login']").click()

# Enter Login details
driver.find_element('name', ConfigReader.Read_Elements('Login','User_Name')).send_keys('Rutuja')
driver.find_element('name', ConfigReader.Read_Elements('Login','U_Pass')).send_keys('rutu')

# Click on Login button
driver.find_element("xpath", "//input[@value ='Login']").click()

# Go to Delete menu in My Accounts menu
driver.find_element('xpath',"//a[contains(text(), 'My Account')]").click()
driver.find_element('xpath',"//a[contains(text(), 'Delete')]").click()

# Multiple window handling
all_windows = driver.window_handles
# print(all_windows)
mainWin = ""

for win in all_windows:
    driver.switch_to.window(win)
    if driver.current_url == "https://www.thetestingworld.com/testings/manage_customer.php":
        time.sleep(5)
        driver.find_element('xpath', "//button[text()='Start Download']").click()
        driver.close()
    else:
        mainWin = win

driver.switch_to.window(mainWin)
# print(driver.current_url)
# input('wait')
