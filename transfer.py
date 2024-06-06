import os
import shutil

# Diretório onde os arquivos são inicialmente baixados (ex. pasta de downloads padrão do navegador)
diretorio_downloads = '/caminho/para/diretorio/de/downloads'

# Caminho do diretório onde deseja mover os arquivos
diretorio_destino = '/caminho/para/seu/diretorio'

# Nomes dos arquivos que foram baixados
nomes_arquivos = [
    'primeiro_arquivo.xlsx',
    'segundo_arquivo.xlsx'
]

# Cria o diretório de destino se não existir
os.makedirs(diretorio_destino, exist_ok=True)

# Lista para armazenar os caminhos dos arquivos copiados
caminhos_dos_arquivos = []

# Copiar os arquivos do diretório de downloads para o diretório de destino
for nome_arquivo in nomes_arquivos:
    caminho_origem = os.path.join(diretorio_downloads, nome_arquivo)
    caminho_destino = os.path.join(diretorio_destino, nome_arquivo)
    shutil.copy(caminho_origem, caminho_destino)
    caminhos_dos_arquivos.append(caminho_destino)

# Exibir os caminhos dos arquivos copiados
print(f'Caminhos dos arquivos copiados: {caminhos_dos_arquivos}')

####

# Espera pelo download começar
time.sleep(5)

# Verifica se o botão "Manter" está presente e clica nele
try:
    keep_button = driver.find_element(By.XPATH, '//a[text()="Manter"]')
    keep_button.click()
    time.sleep(5)  # Espera pelo download completar
except:
    print("Botão 'Manter' não encontrado.")

