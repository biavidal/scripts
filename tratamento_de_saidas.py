import re

class TelnetOutputParser:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.conteudo = self.ler_arquivo()

    def ler_arquivo(self):
        """Lê o conteúdo do arquivo .txt"""
        with open(self.caminho_arquivo, 'r') as arquivo:
            return arquivo.read()

    def separar_comandos(self):
        """Separa comandos e suas saídas no arquivo"""
        padrao_comando = r"(\bshow [a-z]+\b)"  # Padrão genérico para comandos como "show log", "show something"
        comandos = re.split(padrao_comando, self.conteudo)
        return comandos

    def filtrar_logs(self, logs):
        """Filtra logs que seguem o padrão de data e hora"""
        padrao_log = r"^\w{3}\s\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3}:.*$"  # Padrão para logs no formato de data e hora
        linhas_log = logs.splitlines()
        logs_filtrados = [linha for linha in linhas_log if re.match(padrao_log, linha)]
        return logs_filtrados

    def tratar_comando(self, comando, saida):
        """Trata diferentes comandos de acordo com o tipo"""
        if "show log" in comando:
            return self.filtrar_logs(saida)  # Trata a saída de "show log"
        # Aqui você pode adicionar tratamentos para outros comandos específicos
        # if "show ip interface" in comando:
        #     return self.tratar_ip_interface(saida)
        else:
            return saida.splitlines()  # Para outros comandos, apenas retorna as linhas separadas

    def processar_comandos(self):
        """Processa todos os comandos e suas saídas"""
        comandos = self.separar_comandos()
        saidas_tratadas = []
        for i in range(1, len(comandos), 2):  # Índices ímpares são os comandos, pares as saídas
            comando = comandos[i]
            saida = comandos[i + 1].strip()
            saida_tratada = self.tratar_comando(comando, saida)
            saidas_tratadas.append({
                "comando": comando,
                "saida": saida_tratada
            })
        return saidas_tratadas

    def obter_saidas_tratadas(self):
        """Retorna uma lista de todas as saídas tratadas"""
        return self.processar_comandos()

# Exemplo de uso
caminho_arquivo = 'saida_telnet.txt'
parser = TelnetOutputParser(caminho_arquivo)
saidas_tratadas = parser.obter_saidas_tratadas()

# Exibindo as saídas tratadas
for item in saidas_tratadas:
    print(f"Comando: {item['comando']}")
    print("Saída Tratada:")
    for linha in item['saida']:
        print(linha)
    print("-" * 40)
