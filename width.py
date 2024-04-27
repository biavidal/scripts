import pandas as pd

def ajustar_largura_colunas(df):
    # Cria um dicionário para armazenar as larguras ajustadas
    largura_colunas = {}

    # Itera sobre as colunas do DataFrame
    for col in df.columns:
        # Calcula a largura máxima de cada coluna
        largura_maxima = max(df[col].astype(str).apply(len).max(), len(col))
        
        # Adiciona 2 caracteres adicionais para uma margem
        largura_ajustada = largura_maxima + 2
        
        # Armazena a largura ajustada para a coluna
        largura_colunas[col] = largura_ajustada

    return largura_colunas

dados_mean = {"Data" : ['aaaaa', 'aaaaa', 'aaaaaa'],
                  "": ['bbbbb', 'bbbbbb', 'bbbbbb'],
                  "January": ['cccccc', 'cccccc', 'cccccc'],
                  "February": ['ddddd', 'ddddd', 'ddddd'],
                  "March": ['eeeeee', 'eeeeee', 'eeeee']}

dados_rate = {"Tabela" : ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaa'],
              "Rate": ['bbbbb', 'bbbbbb', 'bbbbbb', 'bbbbbbbb', 'bbbbbbb', 'bbbbbbb'],
              "January": ['cccccc', 'cccccc', 'cccccc', 'cccccccc', 'ccccccc', 'cccccccc'],
              "February": ['dddddddd', 'ddddd', 'ddddd', 'dddddddd', 'dddddddd', 'dddddddd'],
              "March": ['eeeeee', 'eeeeee', 'eeeee', 'eeeeee', 'eeeeee', 'eeeeee']}

df_mean = pd.DataFrame(dados_mean)
df_rate = pd.DataFrame(dados_rate)
ajustar_largura_colunas(df_mean)
ajustar_largura_colunas(df_rate)
# Imprime o DataFrame resultante
with pd.ExcelWriter('dados_usd.xlsx', engine='xlsxwriter') as writer:
    df_mean.to_excel(writer, index=False, startrow=2, sheet_name='Resumo')
    df_mean.to_excel(writer, index=False, startrow=7, sheet_name='Resumo')