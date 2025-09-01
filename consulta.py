from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

load_dotenv()

def selecionar_porcentagem_cpu(mensagem_select):
    config = {
        'user': os.getenv("USER_DB"),
        'password': os.getenv("PASSWORD_DB"),
        'host': os.getenv("HOST_DB"),
        'database': os.getenv("DATABASE_DB")
    }

    try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.server_info
            print('Connected to MySQL server version -', db_info)
            
            with db.cursor() as cursor:
                cursor.execute(mensagem_select)
                resultado = cursor.fetchall() 
                
            cursor.close()
            db.close()
            return resultado
    
    except Error as e:
        print('Error to connect with MySQL -', e) 

usuario = ""
mensagem_select = ""

while True: 
    usuario = input("Informe o usuário que deseja visualizar as informações: ")

    h = input("""
        --------------------------------------------------------------------------
        💻O que você deseja fazer?💻
        1- Visualizar todos os dados capturados
        2- Visualizar apenas o horário e os dados da CPU
        3- Visualizar apenas o horário e os dados da memória RAM
        4- Visualizar apenas o horário e os dados da memória de Disco
        q- Sair
        --------------------------------------------------------------------------
        """)

    if h == "1":
        for linha in selecionar_porcentagem_cpu(f"SELECT * FROM capturas where nome_usuario = '{usuario}';"):
            print(f"Usuário: {linha[5]} | CPU: {linha[1]}% | RAM: {linha[2]}% | Disco: {linha[3]} | Data: {linha[4]}");
    elif h == "2":
        for linha in selecionar_porcentagem_cpu(f"select processamento, dtCaptura from capturas where nome_usuario = '{usuario}';"):
            print(f"CPU: {linha[0]}% | Data: {linha[1]}")
    elif h == "3":
        for linha in selecionar_porcentagem_cpu(f"select memoriaRAM, dtCaptura from capturas where nome_usuario = '{usuario}';"):
            print(f"RAM: {linha[0]}% | Data: {linha[1]}")
    elif h == "4":
        for linha in selecionar_porcentagem_cpu(f"select memoriaDisco, dtCaptura from capturas where nome_usuario = '{usuario}';"):
            print(f"Disco: {linha[0]}% | Data: {linha[1]}")
    elif h == "q":
        print("Obrigada por utilizar o meu programa👋🚶")
        break