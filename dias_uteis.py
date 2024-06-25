import pandas as pd
import numpy as np

# Carregar os feriados de um arquivo CSV
feriados = pd.read_csv('feriados.csv', parse_dates=['date'])
feriados_list = feriados['date'].dt.strftime('%Y-%m-%d').tolist()

# Carregar o DataFrame com as datas de requisição
data = {
    'request_date': ['2023-06-23', '2023-06-28', '2023-07-01'],
}
df = pd.DataFrame(data)
df['request_date'] = pd.to_datetime(df['request_date'])

# Função para adicionar 3 dias úteis a uma data
def adicionar_dias_uteis(data_inicial, dias_para_adicionar, feriados_list):
    data_inicial_np = np.datetime64(data_inicial)
    data_final_np = np.busday_offset(data_inicial_np, dias_para_adicionar, holidays=feriados_list)
    return pd.Timestamp(data_final_np)

# Aplicar a função ao DataFrame
df['final_date'] = df['request_date'].apply(lambda x: adicionar_dias_uteis(x, 3, feriados_list))
df['month'] = df['final_date'].dt.month

print(df)