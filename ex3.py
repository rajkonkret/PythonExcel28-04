import openpyxl

wb = openpyxl.load_workbook('./data/videogamesales.xlsx')
ws = wb.active
print(ws)

ws = wb['vgsales']

print("Total number of rows: " + str(ws.max_row))  # total number of rows: 16328
print("Total number of columns: " + str(ws.max_column))  # Total number of columns: 10

print("Value in cell A1 is:", ws['A1'].value)  # Value in cell A1 is: Rank

values = [ws.cell(row=1, column=i).value for i in range(1, ws.max_column)]
print(values)
# ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales']
