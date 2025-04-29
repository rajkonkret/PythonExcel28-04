import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

technologies = ['Spark', "Pandas", 'Python', 'PHP']
fee = [25000, 20000, 15000, 18000]
duration = ['50 Days', '35 Days', np.nan, '15 Days']
discount = [2000, 1000, 500, 500]

data = {
    "Courses": technologies,
    "Fee": fee,
    "Duration": duration,
    "Discount": discount
}

df = pd.DataFrame(data)
print(df)
#   Courses    Fee Duration  Discount
# 0   Spark  25000  50 Days      2000
# 1  Pandas  20000  35 Days      1000
# 2  Python  15000      NaN       500
# 3     PHP  18000  15 Days       500

plt.figure(figsize=(10,6))
bar_width = 0.35
index = np.arange(len(df["Courses"]))

# słupki dla opłat
plt.bar(index, df['Fee'], bar_width, label='Fee', color="blue")

# słupki dla rabatów
plt.bar(index + bar_width, df["Discount"], bar_width, label="Discount", color="red")

# opis  wykresu
plt.title("Course Fees and Discounts")
plt.xlabel("Courses")
plt.ylabel("Amount")
plt.xticks(index + bar_width /2, df["Courses"])

# dodanie legendy
plt.legend()

# wyswietlenie
plt.show()