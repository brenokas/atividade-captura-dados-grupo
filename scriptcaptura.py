from mysql.connector import connect, Error

mensagem_select = ""

def selecionar_porcentagem_cpu():

    config = {
      'user': "root",
      'password': "urubu100",
      'host': 'localhost',
      'database': "oberoncaptura"
    }

    try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.server_info
            print('Connected to MySQL server version -', db_info)
            
            with db.cursor() as cursor:
                query = mensagem_select
                cursor.execute(query)
                resultado = cursor.fetchall() 
                
            cursor.close()
            db.close()
            return resultado
    
    except Error as e:
        print('Error to connect with MySQL -', e) 

booleano = True
exibicao = ""

usuario = ""
while booleano: 
    usuario = input("Informe o usuário que deseja visualizar as informações:")

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
        mensagem_select = "SELECT * FROM capturas where nome_usuario = '{usuario}';"
    elif h == "2":
        mensagem_select = "select processamento, dtCaptura from capturas;"
    elif h == "3":
        mensagem_select = "select memoriaRAM, dtCaptura from capturas;"
    elif h == "4":
        mensagem_select = "select memoriaDisco, dtCaptura from capturas;"
    elif h == "q":
        booleano = False
        print("Obrigada por utilizar o meu programa👋🚶")
        exit()


    resultado = selecionar_porcentagem_cpu()

    for linha in resultado:
        if h == "1":
            print(f"Dados CPU: {linha[1]}%, dados RAM {linha[2]}%, dados disco: {linha[3]}%, Hora da captura {linha[4]}")
        elif h == "2":
            print(f"Dados CPU: {linha[0]}%, Hora da captura: {linha[1]}")
        elif h == "3":
            print(f"Dados RAM: {linha[0]}%, Hora da captura: {linha[1]}")
        elif h == "4":
            print(f"Dados disco: {linha[0]}%, Hora da captura: {linha[1]}")