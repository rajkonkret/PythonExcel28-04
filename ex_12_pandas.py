import pandas as pd

# pip install pandas
# pip install xlsxwriter

# tylko do tworzenia nowych plików
# dość szybka
# tylko xlsx

writer = pd.ExcelWriter('data/empty_file.xlsx')
empty_dataframe = pd.DataFrame()
empty_dataframe.to_excel(writer, sheet_name='empty')
writer.close()
