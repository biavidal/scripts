import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Border, Side

# Crie dois dataframes de exemplo
df1 = pd.DataFrame({
    'Metal': ['Copper', 'Gold', 'Silver'],
    'Data': ['25-01-03', '26-01-03', '27-01-03'],
    'Buyer': ['eBay', 'Amazon', 'Alibaba']
})

df2 = pd.DataFrame({
    'Metal': ['Platinum', 'Palladium', 'Rhodium'],
    'Data': ['28-01-03', '29-01-03', '30-01-03'],
    'Buyer': ['Walmart', 'JD.com', 'Taobao']
})

# Concatene os dataframes verticalmente com duas linhas em branco entre eles
empty_rows = pd.DataFrame([[''] * len(df1.columns)] * 2, columns=df1.columns)
combined_df = pd.concat([df1, empty_rows, df2])

# Crie um escritor de Excel
writer = pd.ExcelWriter('borders.xlsx', engine='openpyxl')

# Escreva o dataframe combinado no Excel
combined_df.to_excel(writer, sheet_name='Sheet1', index=False)

# Adicione bordas à planilha do Excel
workbook = writer.book
sheet = workbook['Sheet1']

border = Border(left=Side(style='thin'),
                right=Side(style='thin'),
                top=Side(style='thin'),
                bottom=Side(style='thin'))

for row in sheet.iter_rows():
    for cell in row:
        cell.border = border

# Salve o arquivo Excel
writer._save()

print("Os dataframes combinados foram salvos como combined_dataframes_with_borders.xlsx com bordas.")
