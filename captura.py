from dotenv import load_dotenv
from mysql.connector import connect, Error
import psutil as p
import os

load_dotenv()

def menu():
  print("\nSelecione a opção desejada:")
  print("1 - Visualizar todos os dados capturados")
  print("2 - Visualizar apenas os timestamps e dados de CPU")
  print("3 - Visualizar apenas os timestamps e dados de RAM")
  print("4 - Visualizar apenas os timestamps e dados de Disco")
  print("7 - Encerrar programa")

def inserir_metricas(porcentagem_cpu, porcentagem_ram, porcentagem_disco, nome_usuario):
  config = {
    'user': os.getenv("USER_DB"),
    'password': os.getenv("PASSWORD_DB"),
    'host': os.getenv("HOST_DB"),
    'database': os.getenv("DATABASE_DB")
    }
  
  try:
    db = connect(**config)

    if (db.is_connected):
      db_info = db.server_info
      print(f"Connected to MySQL server version - {db_info}")

      with db.cursor() as cursor:
        query = "INSERT INTO capturas (processamento, memoriaRAM, memoriaDisco, dtCaptura, nome_usuario) VALUES (%s, %s, %s, now(), %s);"
        value = (porcentagem_cpu, porcentagem_ram, porcentagem_disco, nome_usuario)
        cursor.execute(query, value)

        db.commit()
        print(f"{cursor.rowcount} - registro inserido")
      
      cursor.close()
      db.close()

  except Error as e:
    print(f"Error to connect with MySQL - {e}")

for i in range(20):
  porcentagem_cpu = p.cpu_percent(interval=1, percpu=False)
  porcentagem_ram = p.virtual_memory().percent
  porcentagem_disco = p.disk_usage("/").percent
  nome_usuario = p.users()[0][0]

  print(f"Porcentagem de uso da CPU: {porcentagem_cpu}%")
  print(f"Porcentagem de uso da RAM: {porcentagem_ram}%")
  print(f"Porcentagem de uso do DISCO: {porcentagem_disco}%")
  print(f"Usuário: {nome_usuario}")

  inserir_metricas(porcentagem_cpu, porcentagem_ram, porcentagem_disco, nome_usuario)
