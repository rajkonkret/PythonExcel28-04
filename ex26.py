import pandas as pd

df = pd.DataFrame({
    "Imię": ["Anna", 'Tomek', "Jan", "Anna", 'Jan'],
    "Miasto": ["Kraków", 'Warszawa', 'Gdańsk', 'Kraków', "Gdańsk"],
    "Wynik": [88, 95, 70, 91, 60]
})

df_sorted = df.sort_values(by="Imię")
print(df_sorted.head)
# <bound method NDFrame.head of     Imię    Miasto  Wynik
# 0   Anna    Kraków     88
# 3   Anna    Kraków     91
# 2    Jan    Gdańsk     70
# 4    Jan    Gdańsk     60
# 1  Tomek  Warszawa     95>

df_sorted_2 = df.sort_values(by="Wynik", ascending=False)
print(df_sorted_2.head)

# <bound method NDFrame.head of     Imię    Miasto  Wynik
# 1  Tomek  Warszawa     95
# 3   Anna    Kraków     91
# 0   Anna    Kraków     88
# 2    Jan    Gdańsk     70
# 4    Jan    Gdańsk     60>

df_sorted3 = df.sort_values(by=['Miasto', 'Wynik'], ascending=[True, False])
print(df_sorted3.head)
# <bound method NDFrame.head of     Imię    Miasto  Wynik
# 2    Jan    Gdańsk     70
# 4    Jan    Gdańsk     60
# 3   Anna    Kraków     91
# 0   Anna    Kraków     88
# 1  Tomek  Warszawa     95>

df_grouped = df.groupby("Imię", as_index=False)["Wynik"].mean()
print(df_grouped)
#     Imię  Wynik
# 0   Anna   89.5
# 1    Jan   65.0
# 2  Tomek   95.0

df_sum = df.groupby("Imię", as_index=False)["Wynik"].sum()
print(df_sum)
#     Imię  Wynik
# 0   Anna    179
# 1    Jan    130
# 2  Tomek     95

df_count = df.groupby('Imię').size().reset_index(name="Ilość wpisów")
print(df_count)
#     Imię  Ilość wpisów
# 0   Anna             2
# 1    Jan             2
# 2  Tomek             1
with pd.ExcelWriter('raport.xlsx', engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Oryginalne", index=False)
    df_sorted.to_excel(writer, sheet_name="Posortowane", index=False)
    df_grouped.to_excel(writer, sheet_name="Średnie", index=False)
