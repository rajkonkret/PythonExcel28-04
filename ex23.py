# pip install pyexcel pyexcel-xlsx
import pyexcel as pe

data = [
    ['Imię', "Wiek"],
    ['Tomek', 28],
    ["Kasia", 32]
]

sheet = pe.Sheet(data)
sheet.save_as('wynik.xlsx')

sheet = pe.get_sheet(file_name='wynik.xlsx')
print(sheet)
