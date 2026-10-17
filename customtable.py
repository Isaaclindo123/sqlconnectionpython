# Imports
import sys
import urllib
import pandas as pd
import pyodbc
from sqlalchemy import create_engine

# Inputs
cln1 = input("Digite o nome da coluna 1 na tabela: ")
cln2 = input("Digite o nome da coluna 2 na tabela: ")
cln3 = input("Digite o nome da coluna 3 na tabela: ")
print("FEITO! Agora, digite os dados presentes nessas colunas: ")
print("")
dds1 = input("Digite o dado da coluna 1 na tabela: ")
dds2 = input("Digite o dado da coluna 2 na tabela: ")
dds3 = input("Digite o dado da coluna 3 na tabela: ")
apndorrepl = input("Fale se vc quer que o programa adiciona os dados [1] ou se quer substituir os dados [2]: ")
if apndorrepl == "1":
    print("OK, iremos adicionar os dados")
    ied = "append"
elif apndorrepl == "2":
    print("OK, iremos substituir os dados")
    ied = "replace"
else:
    print("Escreva um número válido")
    input("> ")
    sys.exit()

print("PRONTO!! Aguarte uns milisegundos para que os dados sejam inseridos...")

# No DB
# 1. Criar seus dados no Python (Exemplo de DataFrame)
dados = {
    cln1: [dds1],
    cln2: [dds2],
    cln3: [dds3],
}
df = pd.DataFrame(dados)

# 2. Configurar a conexão adaptada para o SQLAlchemy
params = urllib.parse.quote_plus(
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=MEU_COMPUTADOR\SQLEXPRESS;"
    r"Database=Python Spower;"
    r"Trusted_Connection=yes;"
)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# 3. Enviar o DataFrame completo para o SQL Server
try:
  # name = nome da tabela no SQL Server
  # if_exists = 'append' adiciona os dados / 'replace' recria a tabela do zero
  # index = False evita enviar o índice do Pandas como coluna
  df.to_sql(name="TabeladeTestedeDados", con=engine, if_exists=ied, index=False)
  print("Ação concluída com êxito")
except Exception as e:
  print(f"Erro na ação: {e}")

# Trava de segurança se vc estiver no python launcher (dando 2 cliques no arquivo)

print("To exit, press enter, if you is in launcher")
input("> ")
