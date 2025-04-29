# xlrd - czytania plików xls
# xlwt - zapis do pliku xls
import xlwt

# pip install xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Dane")

sheet.write(0, 0, "Imię")
sheet.write(0, 1, "Wiek")
sheet.write(1, 0, "Jan")
sheet.write(1, 1, 28)

workbook.save('plik_xlwt.xls')
