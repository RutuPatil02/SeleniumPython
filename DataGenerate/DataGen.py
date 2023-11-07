import openpyxl


# Data Driven Testing
def dataGenerator():
    # Hardcoded data list
    li = [['user1', 'pass1'], ['user2', 'pass2'], ['user3', 'pass3']]

    # Generate data from Excel file
    #wk = openpyxl.load_workbook('D://RegData.xlsx')
    #sh = wk['Sheet1']
    #r = sh.max_row
    #li = []
    #lil = []

    #for r in range(1, r+1):
    #    lil = []
    #    un = sh.cell[r, 1]
    #    up = sh.cell[r, 2]
    #    lil.insert(0, un.value)
    #    lil.insert(1, up.value)
    #    li.insert(r-1, lil)

    return li

