import telnetlib
import pandas as pd
from datetime import datetime

# Defina as variáveis de conexão Telnet
host = 'example.com'
port = 23
username = 'your_username'
password = 'your_password'

# Lista de comandos para executar
commands = [
    'command_1',
    'command_2',
    'command_3'
]

# Dicionário para armazenar os resultados dos comandos, tempos e IPs
results = []
ip_address = '192.168.1.1'  # Defina o IP relacionado aos comandos

# Conectando ao Telnet
tn = telnetlib.Telnet(host, port)

# Realizando login (se necessário)
tn.read_until(b"login: ")
tn.write(username.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

# Função para capturar saídas longas com interação
def capture_long_output(command, tn, prompt=b"$", more_indicator=b"--More--"):
    output = b""
    tn.write(command.encode('ascii') + b"\n")
    
    while True:
        partial_output = tn.read_until(more_indicator, timeout=5)
        output += partial_output
        
        if more_indicator in partial_output:
            # Enviar espaço ou enter para continuar a exibição
            tn.write(b" ")
        else:
            break
    
    # Ler qualquer saída restante até o prompt do sistema
    output += tn.read_until(prompt)
    return output.decode('ascii')

# Executando cada comando, capturando o tempo e a saída
for command in commands:
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Captura o horário de início
    output = capture_long_output(command, tn)
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Captura o horário de término
    
    # Adiciona os resultados ao dicionário com o comando, IP, horários e saída
    results.append({
        'Command': command,
        'IP': ip_address,
        'Start Time': start_time,
        'End Time': end_time,
        'Output': output
    })

# Fechando a conexão Telnet
tn.close()

# Convertendo os resultados em um DataFrame do pandas
df = pd.DataFrame(results)

# Salvando o DataFrame em um arquivo Excel
df.to_excel('telnet_outputs.xlsx', index=False)

print("Saídas dos comandos foram salvas em telnet_outputs.xlsx")
