import mysql.connector

class Conexao: 

    def criar_conexao():
        # Criando a coneção 

        conexao = mysql.connector.connect(
            host = "localhost", port = 3306,
            user = "root",
            password = "root",
            database = "feedback"
        )
        
        return conexao