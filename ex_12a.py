import pandas as pd

data = [
    ["Aditya", 179],
    ['Sameer', 181],
    ['Darwin', 170],
    ["Joel", 167]
]

column_names = ['Name', 'Hight']

df = pd.DataFrame(data, columns=column_names)
writer = pd.ExcelWriter('excel_with_list.xlsx', engine='xlsxwriter')

# df.to_excel(writer, sheet_name='first_sheet')
# df.to_excel(writer, sheet_name='first_sheet', index=False)
# df.to_excel(writer, sheet_name='first_sheet', index=False, startrow=3)
# df.to_excel(writer, sheet_name='first_sheet', index=False, startcol=4)
df.to_excel(writer, sheet_name='first_sheet', index=False, startrow=3, startcol=4)
writer.close()
