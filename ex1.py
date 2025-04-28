import openpyxl
# pip install openpyxl

wb = openpyxl.load_workbook("./data/videogamesales.xlsx")

print(wb)