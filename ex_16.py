import pandas as pd

height_data = [
    {"Name": "Aditya", "Height": 179},
    {"Name": "Sameer", "Height": 181},
    {"Name": "Darwin", "Height": 170},
    {"Name": "Aditya", "Height": 167},
]

weight_data = [
    {"Name": "Aditya", "Weight": 76},
    {"Name": "Sameer", "Weight": 68},
    {"Name": "Darwin", "Weight": 69},
    {"Name": "Aditya", "Weight": 73},
]

marks_data = [
    {"Name": "Aditya", "Marks": 179},
    {"Name": "Sameer", "Marks": 181},
    {"Name": "Darwin", "Marks": 170},
    {"Name": "Aditya", "Marks": 167},
]

height_data_df = pd.DataFrame(height_data)
weight_data_df = pd.DataFrame(weight_data)
marks_data_df = pd.DataFrame(marks_data)

writer = pd.ExcelWriter('data/excel_with_multiple_sheets.xlsx', engine='xlsxwriter')

height_data_df.to_excel(writer, sheet_name='height', index=False)
weight_data_df.to_excel(writer, sheet_name='weight', index=False)
marks_data_df.to_excel(writer, sheet_name='marks', index=False)

writer.close()


