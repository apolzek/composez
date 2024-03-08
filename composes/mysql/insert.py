import mysql.connector

def create_database_and_insert_records():
    # Conecta ao banco de dados MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password'
    )

    cursor = connection.cursor()

    # Cria o banco de dados 'testing' se ele não existir
    cursor.execute("CREATE DATABASE IF NOT EXISTS testing")
    
    # Seleciona o banco de dados 'testing'
    connection.database = 'testing'

    # Cria uma tabela 'example' se ela não existir
    cursor.execute("CREATE TABLE IF NOT EXISTS example (id INT AUTO_INCREMENT PRIMARY KEY, value INT)")

    # Insere 1000 registros na tabela 'example'
    for i in range(1, 1001):
        cursor.execute("INSERT INTO example (value) VALUES (%s)", (i,))

    # Confirma as alterações no banco de dados
    connection.commit()

    # Fecha o cursor e a conexão
    cursor.close()
    connection.close()

    print("1000 registros inseridos com sucesso.")

if __name__ == "__main__":
    create_database_and_insert_records()
