import xlrd

# pip install xlrd

workbook = xlrd.open_workbook('plik_xlwt.xls')
sheet = workbook.sheet_by_index(0)

print(sheet.cell_value(0, 0))
print(sheet.cell_value(1, 0))
# Imię
# Jan
