#openpyxl
from openpyxl import Workbook
Spreadsheet = Workbook()

# grab the active worksheet
worksheet = Spreadsheet.active

# Data can be assigned directly to cells
worksheet['A1'] = 50

# Rows can also be appended
worksheet.append([5, 15, 25, 35, 45, 55])
worksheet.append([9, 19, 29, 39, 49, 59])

# Python types will automatically be converted
import datetime
t1 = datetime.datetime.now()
worksheet['A1'] = t1.year
worksheet['A2'] = t1

# Save the file
Spreadsheet.save("E:\\openpyxl.xlsx")
