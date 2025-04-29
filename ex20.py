import pandas as pd

df = pd.read_excel('data/excel_without_index-1.xlsx')
print(df)

print(df[df['Height'] > 175])
#      Name  Height
# 0  Aditya     179
# 1  Sameer     181
suma = df['Height'].sum(skipna=False)  # skipna - omin brakujące
print("Suma:", suma)
# Suma: 697
print(df.info)
# <bound method DataFrame.info of        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167>

print(df.describe)
# <bound method NDFrame.describe of        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167>
