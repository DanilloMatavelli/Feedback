from hashlib import sha256

from flask import session
from data.conexao import Conexao
import datetime

# Classe para cadastrar usuario
class Usuario: 
    def cadastrarUsuario(login, usuario, senha):
        # Criptografando a senha 
        senha = sha256(senha.encode()).hexdigest()

        # CADASTRANDO AS INFORMAÇÕES NO BANCO DE DADOS
        # Criando a coneção 

        conexao = Conexao.criar_conexao()

        # O cursor será responsavel por manipular o banco de dados 
        cursor = conexao.cursor()

        # Criando o SQL que será executado 
        sql = """INSERT INTO tb_usuarios
                    (login, nome, senha)
                VALUES
                    (%s, %s, %s)"""
        
        valores = (login, usuario , senha)

        # Executando o comando SQL
        cursor.execute(sql,valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexão com o Banco
        cursor.close()
        conexao.close()
        
    def verificarLogin(login, senha):
        senha = sha256(senha.encode()).hexdigest()
        
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()

        # Criando o SQL para buscar o usuário e senha
        sql = """SELECT login, nome FROM tb_usuarios
                    WHERE login = %s
                    AND binary senha = %s;"""
        
        valores = (login, senha)

        cursor.execute(sql, valores)

        # fetchone retorna apenas um valor 
        resultado = cursor.fetchone()

        # Fecho a conexão e o cursor com o Banco
        cursor.close()
        conexao.close()

        # Verifica se o usuario está corretor, se tiver retorna True, senão retorne false
        if resultado:
            # Peguei o login e coloquei dentro da sessão usuario
            session['usuario'] = resultado[0] 
            # Peguei o nome e coloquei dentro da sessão nome_usuario
            session['nome_usuario'] = resultado[1]  
            return True
        else:
            return False

    def logoff():
        session.clear()
       