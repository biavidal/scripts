import pandas as pd
import numpy as np

df_master = pd.read_excel(r'c:\Users\Thay\Documents\testeMapa\mapaMaster.xlsx')
df_update = pd.read_excel(r'c:\Users\Thay\Documents\testeMapa\atualizacaoMapa.xlsx')
columns = df_update.iloc[:, 0:4] 

df_update = df_update.reindex(df_master.index, fill_value=np.nan)

df_update['cpf'] = df_master['cpf']

display(df_master)
display(df_update)