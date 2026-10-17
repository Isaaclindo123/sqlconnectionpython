# Imports
import urllib
import pandas as pd
import pyodbc
from sqlalchemy import create_engine

# Inputs
username = input("Digite seu nome de usuário: ")
pswrd = input("Digite sua senha: ")

# No DB
# 1. Criar seus dados no Python (Exemplo de DataFrame)
dados = {
    "ID": [1],
    "Usuário": [username],
    "Senha": [pswrd],
}
df = pd.DataFrame(dados)

# 2. Configurar a conexão adaptada para o SQLAlchemy
params = urllib.parse.quote_plus(
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=NOME_COMPUTADOR\SQLEXPRESS;"
    r"Database=Python Spower;"
    r"Trusted_Connection=yes;"
)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# 3. Enviar o DataFrame completo para o SQL Server
try:
  # name = nome da tabela no SQL Server
  # if_exists = 'append' adiciona os dados / 'replace' recria a tabela do zero
  # index = False evita enviar o índice do Pandas como coluna
  df.to_sql(name="PasswordSystem1", con=engine, if_exists="append", index=False)
  print("Ação concluída com êxito")
except Exception as e:
  print(f"Erro na ação: {e}")

# Trava de segurança se vc estiver no python launcher (dando 2 cliques no arquivo)

print("To exit, press enter, if you is in launcher")
input("> ")
