from Library import ConfigReader


class RegistrationClass:
    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username):
        driver.find_element('name', ConfigReader.Read_Elements('Registration', 'User_Name')).send_keys(username)

    def enter_email(self, email):
        driver.find_element('name', ConfigReader.Read_Elements('Registration', 'Email_ID')).send_keys(email)

    def enter_pswd(self, password):
        driver.find_element('name', ConfigReader.Read_Elements('Registration', 'U_Pass')).send_keys(password)
