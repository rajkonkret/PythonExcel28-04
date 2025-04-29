import pandas as pd

# df = pd.read_excel("data/excel_with_multiple_sheets-1.xlsx", sheet_name=2)
# print(df)
#        Name  Marks
# 0    Aditya     79
# 1    Sameer     81
# 2  Dharwish     70
# 3      Joel     67
df = pd.read_excel("data/excel_with_multiple_sheets-1.xlsx", sheet_name="marks")
print(df)
#        Name  Marks
# 0    Aditya     79
# 1    Sameer     81
# 2  Dharwish     70
# 3      Joel     67

data = pd.ExcelFile('data/excel_with_multiple_sheets-1.xlsx')
print(data.sheet_names)  # ['height', 'weight', 'marks']

df = pd.read_excel("data/excel_with_multiple_sheets-1.xlsx", sheet_name=data.sheet_names[0])
print(df)
#        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167
df = pd.read_excel('data/excel_with_multiple_sheets-1.xlsx', sheet_name="marks", usecols=["Name"])
print(df)
#       Name
# 0    Aditya
# 1    Sameer
# 2  Dharwish
# 3      Joel

df = data.parse("height")
print(df.head())  # pięć pierwszych wierszy

#        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167
print(df.tail())  # 5 ostatnich
#        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167

print(df.columns)
print(df.columns.tolist())
# Index(['Name', 'Height'], dtype='object')
# ['Name', 'Height']
