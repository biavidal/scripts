from openpyxl.styles import Border, Side
from openpyxl.utils import get_column_letter

def apply_border_to_dataframe(sheet, df, start_row_data, start_row_first_row):
    # Define o estilo de borda para a primeira linha
    border_style_first_row = Border(
        top=Side(style='thin'),
        bottom=Side(style='thin'),
        left=Side(style='thin'),
        right=Side(style='thin')
    )
    
    # Define o estilo de borda para as laterais
    border_style_lateral = Border(
        left=Side(style='thin'),
        right=Side(style='thin')
    )
    
    # Adiciona bordas às primeiras linhas de cada coluna de cada DataFrame
    for column in range(1, len(df.columns) + 1):
        col_letter = get_column_letter(column)
        cell = sheet[col_letter + str(start_row_first_row)]
        cell.border = border_style_first_row
        for row in range(start_row_data, len(df) + start_row_data):
            cell = sheet[col_letter + str(row)]
            cell.border = border_style_lateral